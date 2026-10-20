Add-Type -AssemblyName System.Drawing

$srcPath = "d:\Project\20-10\tulip.png"
$dstPath = "d:\Project\20-10\tulip_transparent.png"

$bmp = [System.Drawing.Bitmap]::new($srcPath)
$width = $bmp.Width
$height = $bmp.Height

# Tạo bitmap mới hỗ trợ kênh Alpha (Format32bppArgb)
$newBmp = [System.Drawing.Bitmap]::new($width, $height, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)

# Dùng LockBits để xử lý siêu nhanh
$rect = [System.Drawing.Rectangle]::new(0, 0, $width, $height)
$bmpData = $bmp.LockBits($rect, [System.Drawing.Imaging.ImageLockMode]::ReadOnly, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
$newBmpData = $newBmp.LockBits($rect, [System.Drawing.Imaging.ImageLockMode]::WriteOnly, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)

$bytes = [Math]::Abs($bmpData.Stride) * $height
$rgbValues = [byte[]]::new($bytes)
$outputValues = [byte[]]::new($bytes)

[System.Runtime.InteropServices.Marshal]::Copy($bmpData.Scan0, $rgbValues, 0, $bytes)

# Mảng đánh dấu visited cho BFS Flood Fill từ biên
$visited = [bool[]]::new($width * $height)
$queue = [System.Collections.Generic.Queue[int]]::new()

# Thêm tất cả pixel viền ngoài (top, bottom, left, right) vào Queue nếu là màu nền (sáng trắng)
function IsBgColor([byte]$b, [byte]$g, [byte]$r) {
    # Nền là màu trắng hoặc gần trắng (R, G, B đều lớn hơn 225)
    return ($r -ge 225 -and $g -ge 225 -and $b -ge 225)
}

for ($x = 0; $x -lt $width; $x++) {
    # Top
    $idxTop = $x
    $byteIdxTop = $idxTop * 4
    if (IsBgColor $rgbValues[$byteIdxTop] $rgbValues[$byteIdxTop + 1] $rgbValues[$byteIdxTop + 2]) {
        $visited[$idxTop] = $true
        $queue.Enqueue($idxTop)
    }
    # Bottom
    $idxBot = ($height - 1) * $width + $x
    $byteIdxBot = $idxBot * 4
    if (IsBgColor $rgbValues[$byteIdxBot] $rgbValues[$byteIdxBot + 1] $rgbValues[$byteIdxBot + 2]) {
        $visited[$idxBot] = $true
        $queue.Enqueue($idxBot)
    }
}

for ($y = 0; $y -lt $height; $y++) {
    # Left
    $idxLeft = $y * $width
    $byteIdxLeft = $idxLeft * 4
    if (-not $visited[$idxLeft] -and (IsBgColor $rgbValues[$byteIdxLeft] $rgbValues[$byteIdxLeft + 1] $rgbValues[$byteIdxLeft + 2])) {
        $visited[$idxLeft] = $true
        $queue.Enqueue($idxLeft)
    }
    # Right
    $idxRight = $y * $width + ($width - 1)
    $byteIdxRight = $idxRight * 4
    if (-not $visited[$idxRight] -and (IsBgColor $rgbValues[$byteIdxRight] $rgbValues[$byteIdxRight + 1] $rgbValues[$byteIdxRight + 2])) {
        $visited[$idxRight] = $true
        $queue.Enqueue($idxRight)
    }
}

# Hướng di chuyển 4 phía
$dx = @(0, 0, 1, -1)
$dy = @(1, -1, 0, 0)

while ($queue.Count -gt 0) {
    $curr = $queue.Dequeue()
    $cx = $curr % $width
    $cy = [Math]::Floor($curr / $width)

    for ($i = 0; $i -lt 4; $i++) {
        $nx = $cx + $dx[$i]
        $ny = $cy + $dy[$i]

        if ($nx -ge 0 -and $nx -lt $width -and $ny -ge 0 -and $ny -lt $height) {
            $nIdx = $ny * $width + $nx
            if (-not $visited[$nIdx]) {
                $bIdx = $nIdx * 4
                $b = $rgbValues[$bIdx]
                $g = $rgbValues[$bIdx + 1]
                $r = $rgbValues[$bIdx + 2]
                
                # Nếu là màu nền nối tiếp
                if ($r -ge 220 -and $g -ge 220 -and $b -ge 220) {
                    $visited[$nIdx] = $true
                    $queue.Enqueue($nIdx)
                }
            }
        }
    }
}

# Tạo output với Alpha mượt mà
for ($i = 0; $i -lt ($width * $height); $i++) {
    $bIdx = $i * 4
    $b = $rgbValues[$bIdx]
    $g = $rgbValues[$bIdx + 1]
    $r = $rgbValues[$bIdx + 2]

    if ($visited[$i]) {
        # Điểm thuộc nền ngoài: tính alpha mượt mà
        $minC = [Math]::Min($r, [Math]::Min($g, $b))
        if ($minC -ge 248) {
            # Hoàn toàn trong suốt
            $outputValues[$bIdx] = 0
            $outputValues[$bIdx + 1] = 0
            $outputValues[$bIdx + 2] = 0
            $outputValues[$bIdx + 3] = 0
        } else {
            # Vùng viền chuyển tiếp mờ mịn (feathered boundary)
            $alphaRatio = (248.0 - $minC) / 28.0
            if ($alphaRatio -lt 0) { $alphaRatio = 0 }
            if ($alphaRatio -gt 1) { $alphaRatio = 1 }
            $alpha = [byte]($alphaRatio * 255)
            
            $outputValues[$bIdx] = $b
            $outputValues[$bIdx + 1] = $g
            $outputValues[$bIdx + 2] = $r
            $outputValues[$bIdx + 3] = $alpha
        }
    } else {
        # Điểm thuộc hoa: giữ nguyên 100% không mất nét
        $outputValues[$bIdx] = $b
        $outputValues[$bIdx + 1] = $g
        $outputValues[$bIdx + 2] = $r
        $outputValues[$bIdx + 3] = 255
    }
}

[System.Runtime.InteropServices.Marshal]::Copy($outputValues, 0, $newBmpData.Scan0, $bytes)

$bmp.UnlockBits($bmpData)
$newBmp.UnlockBits($newBmpData)

# Lưu thành PNG trong suốt
$newBmp.Save($dstPath, [System.Drawing.Imaging.ImageFormat]::Png)

$bmp.Dispose()
$newBmp.Dispose()

Write-Host "Transparent PNG created successfully at: $dstPath"
