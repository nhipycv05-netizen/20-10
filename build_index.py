import os

# Đọc base64 của ảnh tulip đã tách nền trong suốt
with open("tulip_base64.txt", "r", encoding="utf-8") as f:
    tulip_b64 = f.read().strip()

html_content = f'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cả Một Vườn Thương ✦ Chúc Mừng Ngày Phụ Nữ Việt Nam 20/10</title>
  <meta name="description" content="Trang web thiệp hoa kỷ niệm ngày Phụ nữ Việt Nam 20/10 - Cả một vườn thương dành tặng người phụ nữ bạn yêu quý.">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">

  <!-- Confetti CDN -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>

  <style>
    :root {{
      --text-brown: #3f1f25;
      --text-muted: #78484f;
      --card-bg: rgba(255, 255, 255, 0.96);
      --card-border: rgba(255, 255, 255, 0.95);
      --card-shadow: 0 15px 35px rgba(0, 0, 0, 0.12), 0 0 25px rgba(255, 255, 255, 0.9), 0 25px 60px -10px rgba(180, 80, 100, 0.18);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    html, body {{
      height: 100%;
      width: 100vw;
      overflow: hidden; /* Cố định 1 màn hình duy nhất, tuyệt đối không bị cuộn */
    }}

    body {{
      font-family: 'Be Vietnam Pro', sans-serif;
      color: var(--text-brown);
      /* Gradient trong trẻo: Bầu trời xanh sớm mai -> Hồng ngọc trai nhẹ -> Cỏ xanh mờ sương */
      background: linear-gradient(
        180deg,
        #eaf4fc 0%,
        #e0f2fe 18%,
        #fff5f7 42%,
        #fff0f5 65%,
        #edf7ee 86%,
        #e8f5e9 100%
      );
      position: relative;
      user-select: none;
    }}

    /* Soft Glow Vignette & Sunlight Overlay */
    .vignette-overlay {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 1;
      background: radial-gradient(ellipse at 85% 8%, rgba(255, 253, 238, 0.6) 0%, transparent 55%),
                  radial-gradient(circle at 50% 35%, transparent 60%, rgba(215, 235, 248, 0.22) 90%, rgba(195, 222, 238, 0.35) 100%);
    }}

    /* Background Ambient Canvas (Sparkles & Falling Petals) */
    #ambientCanvas {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 1;
    }}

    /* Atmospheric Light Leaks */
    .light-leak {{
      position: fixed;
      border-radius: 50%;
      filter: blur(85px);
      pointer-events: none;
      z-index: 0;
      opacity: 0.65;
      animation: floatAura 18s ease-in-out infinite alternate;
    }}

    .leak-1 {{
      top: -8%;
      left: 8%;
      width: 450px;
      height: 450px;
      background: radial-gradient(circle, rgba(254, 249, 230, 0.75) 0%, rgba(224, 242, 254, 0) 70%);
    }}

    .leak-2 {{
      bottom: -10%;
      left: 15%;
      width: 520px;
      height: 520px;
      background: radial-gradient(circle, rgba(200, 240, 215, 0.45) 0%, rgba(232, 245, 233, 0) 70%);
      animation-delay: -7s;
    }}

    .leak-3 {{
      top: 35%;
      right: 15%;
      width: 380px;
      height: 380px;
      background: radial-gradient(circle, rgba(254, 226, 235, 0.45) 0%, rgba(255, 255, 255, 0) 70%);
      animation-delay: -12s;
    }}

    @keyframes floatAura {{
      0% {{ transform: translate(0, 0) scale(1); }}
      50% {{ transform: translate(28px, -24px) scale(1.1); }}
      100% {{ transform: translate(-24px, 18px) scale(0.95); }}
    }}

    /* Header Bar */
    .top-bar {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px 24px;
      z-index: 100;
      pointer-events: none;
    }}

    .brand-tag {{
      font-family: 'Cormorant Garamond', serif;
      font-style: italic;
      font-size: 1.05rem;
      letter-spacing: 0.08em;
      color: rgba(94, 46, 52, 0.88);
      font-weight: 600;
      background: rgba(255, 255, 255, 0.65);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      padding: 6px 16px;
      border-radius: 30px;
      border: 1px solid rgba(255, 255, 255, 0.85);
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
      pointer-events: auto;
      transition: all 0.3s ease;
    }}

    .brand-tag:hover {{
      background: rgba(255, 255, 255, 0.9);
      transform: translateY(-1px);
    }}

    .audio-btn {{
      pointer-events: auto;
      background: rgba(255, 255, 255, 0.72);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid rgba(255, 255, 255, 0.9);
      padding: 7px 16px;
      border-radius: 30px;
      display: flex;
      align-items: center;
      gap: 9px;
      cursor: pointer;
      box-shadow: 0 4px 18px rgba(110, 40, 50, 0.08);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      color: #642b32;
      font-size: 0.86rem;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-weight: 500;
    }}

    .audio-btn:hover {{
      background: rgba(255, 255, 255, 0.95);
      transform: translateY(-2px);
      box-shadow: 0 6px 22px rgba(110, 40, 50, 0.14);
    }}

    .audio-bars {{
      display: flex;
      align-items: flex-end;
      gap: 2.5px;
      height: 14px;
      width: 16px;
    }}

    .audio-bars span {{
      width: 2.5px;
      background: #c92a2a;
      border-radius: 2px;
      height: 4px;
      transition: height 0.2s ease;
    }}

    .audio-btn.playing .audio-bars span:nth-child(1) {{
      animation: barDance 0.8s ease-in-out infinite alternate;
    }}
    .audio-btn.playing .audio-bars span:nth-child(2) {{
      animation: barDance 1.1s ease-in-out infinite alternate 0.2s;
    }}
    .audio-btn.playing .audio-bars span:nth-child(3) {{
      animation: barDance 0.9s ease-in-out infinite alternate 0.4s;
    }}

    @keyframes barDance {{
      0% {{ height: 3px; }}
      100% {{ height: 14px; }}
    }}

    /* Screen Container: Cố định 100vh không cuộn */
    .app-screen {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      transition: transform 1.2s cubic-bezier(0.22, 1, 0.36, 1), 
                  opacity 1s cubic-bezier(0.22, 1, 0.36, 1);
    }}

    #screen1 {{
      opacity: 1;
      transform: translateY(0);
      z-index: 10;
      padding: 55px 16px 20px;
    }}

    #screen1.hide {{
      opacity: 0;
      transform: translateY(-80px) scale(0.96);
      pointer-events: none;
    }}

    #screen2 {{
      opacity: 0;
      transform: translateY(40px);
      pointer-events: none;
      visibility: hidden;
      z-index: 10;
      padding: 20px 16px;
      transition: transform 1.1s cubic-bezier(0.16, 1, 0.3, 1), 
                  opacity 1.0s cubic-bezier(0.16, 1, 0.3, 1),
                  visibility 0s 1.1s;
    }}

    #screen2.show {{
      opacity: 1;
      transform: translateY(0);
      pointer-events: auto;
      visibility: visible;
      transition: transform 1.1s cubic-bezier(0.16, 1, 0.3, 1), 
                  opacity 1.0s cubic-bezier(0.16, 1, 0.3, 1),
                  visibility 0s 0s;
    }}

    /* =====================================================================
       SCREEN 1: BÔNG HOA TULIP NGHỆ THUẬT & LỜI MỜI
       ===================================================================== */
    .hero-content {{
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      max-width: 600px;
      position: relative;
      z-index: 5;
    }}

    .hero-title {{
      font-family: 'Playfair Display', serif;
      font-size: clamp(2.1rem, 4.5vw, 3.4rem);
      font-weight: 600;
      color: #381a20;
      line-height: 1.2;
      margin-bottom: 8px;
      letter-spacing: -0.01em;
      text-shadow: 0 2px 20px rgba(255, 255, 255, 0.9);
      animation: fadeInDown 1.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}

    .hero-subtitle {{
      font-family: 'Cormorant Garamond', serif;
      font-style: italic;
      font-size: clamp(1.05rem, 2.2vw, 1.35rem);
      color: #723e46;
      letter-spacing: 0.04em;
      margin-bottom: 18px;
      animation: fadeInUp 1.4s cubic-bezier(0.16, 1, 0.3, 1) 0.2s backwards;
    }}

    .sparkle-icon {{
      display: inline-block;
      color: #eab308;
      animation: pulseSparkle 2.2s infinite ease-in-out;
      margin: 0 4px;
    }}

    @keyframes pulseSparkle {{
      0%, 100% {{ transform: scale(1) rotate(0deg); opacity: 0.8; }}
      50% {{ transform: scale(1.35) rotate(15deg); opacity: 1; filter: drop-shadow(0 0 6px #fde047); }}
    }}

    .flower-wrapper {{
      position: relative;
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      margin: 8px 0 18px;
      transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
      animation: floatFlower 6s ease-in-out infinite;
    }}

    .flower-wrapper:hover {{
      transform: scale(1.05) translateY(-5px);
    }}

    .flower-wrapper:active {{
      transform: scale(0.97);
    }}

    .flower-glow {{
      position: absolute;
      top: 30%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 260px;
      height: 260px;
      background: radial-gradient(circle, rgba(244, 114, 182, 0.32) 0%, rgba(254, 205, 211, 0.18) 50%, transparent 75%);
      border-radius: 50%;
      filter: blur(28px);
      pointer-events: none;
      animation: pulseGlow 4s ease-in-out infinite alternate;
      transition: all 0.5s ease;
    }}

    .flower-wrapper:hover .flower-glow {{
      width: 320px;
      height: 320px;
      background: radial-gradient(circle, rgba(244, 114, 182, 0.45) 0%, rgba(251, 191, 36, 0.28) 50%, transparent 75%);
    }}

    @keyframes pulseGlow {{
      0% {{ transform: translate(-50%, -50%) scale(0.92); opacity: 0.6; }}
      100% {{ transform: translate(-50%, -50%) scale(1.15); opacity: 0.95; }}
    }}

    @keyframes floatFlower {{
      0%, 100% {{ transform: translateY(0) rotate(0deg); }}
      50% {{ transform: translateY(-10px) rotate(1.2deg); }}
    }}

    .tulip-watercolor-img {{
      width: clamp(210px, 30vw, 280px);
      height: auto;
      filter: drop-shadow(0 15px 30px rgba(180, 50, 75, 0.22));
      transition: filter 0.4s ease, transform 0.4s ease;
      display: block;
      user-select: none;
      -webkit-user-drag: none;
    }}

    .flower-wrapper:hover .tulip-watercolor-img {{
      filter: drop-shadow(0 20px 36px rgba(225, 29, 72, 0.35)) brightness(1.03);
    }}

    .tulip-sparkles-overlay {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
    }}

    .tap-hint {{
      margin-top: 8px;
      background: rgba(255, 255, 255, 0.78);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.9);
      padding: 8px 20px;
      border-radius: 40px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      color: #63262f;
      font-size: 0.88rem;
      font-weight: 500;
      box-shadow: 0 4px 16px rgba(120, 40, 50, 0.08);
      cursor: pointer;
      transition: all 0.3s ease;
      animation: fadeInUp 1.4s cubic-bezier(0.16, 1, 0.3, 1) 0.4s backwards;
    }}

    .tap-hint:hover {{
      background: rgba(255, 255, 255, 0.95);
      transform: translateY(-2px);
      box-shadow: 0 8px 22px rgba(120, 40, 50, 0.15);
      color: #9f1239;
    }}

    .tap-hint-hand {{
      font-size: 1.05rem;
      animation: gentleTap 1.6s infinite ease-in-out;
    }}

    @keyframes gentleTap {{
      0%, 100% {{ transform: translateY(0); }}
      50% {{ transform: translateY(-3px) scale(1.1); }}
    }}

    /* =====================================================================
       VƯỜN HOA TULIP NỀN: NẰM HOÀN TOÀN Ở LỚP NỀN PHÍA SAU (z-index: 2)
       Chiếm 45% - 50% màn hình, đan xen khít nhau lấp ló 2 bên và dưới chân thiệp
       ===================================================================== */
    .tulip-garden-container {{
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100vw;
      height: 48vh;
      min-height: 360px;
      max-height: 500px;
      pointer-events: none;
      z-index: 2;
      overflow: visible;
      opacity: 0;
      transform: translateY(60px);
      transition: opacity 1.2s ease, transform 1.4s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    #screen2.show ~ .tulip-garden-container,
    .tulip-garden-container.visible {{
      opacity: 1;
      transform: translateY(0);
    }}

    /* Thảm sương cỏ nền */
    .garden-ground-mist {{
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 35%;
      background: linear-gradient(to top, rgba(232, 245, 233, 0.92) 0%, rgba(237, 247, 238, 0.5) 50%, transparent 100%);
      z-index: 1;
      pointer-events: none;
    }}

    .tulip-layer {{
      position: absolute;
      bottom: -15px;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
    }}

    .tulip-layer.deep-back {{
      z-index: 2;
      opacity: 0.78;
      filter: blur(1.2px) brightness(0.95);
      bottom: -30px;
    }}

    .tulip-layer.back {{
      z-index: 3;
      opacity: 0.88;
      filter: blur(0.7px) brightness(0.98);
      bottom: -20px;
    }}

    .tulip-layer.mid {{
      z-index: 4;
      opacity: 0.96;
      filter: drop-shadow(0 8px 16px rgba(50, 100, 70, 0.12));
      bottom: -10px;
    }}

    .tulip-layer.front {{
      z-index: 5;
      opacity: 1;
      filter: drop-shadow(0 14px 24px rgba(40, 80, 60, 0.18));
      bottom: -5px;
    }}

    .tulip-stem {{
      position: absolute;
      bottom: 0;
      transform-origin: bottom center;
      transition: transform 1.2s cubic-bezier(0.34, 1.56, 0.64, 1), 
                  filter 0.8s ease;
      will-change: transform;
      display: flex;
      justify-content: center;
      align-items: flex-end;
    }}

    .tulip-flora-img {{
      height: 100%;
      width: auto;
      display: block;
      user-select: none;
      -webkit-user-drag: none;
      object-fit: contain;
    }}

    .sway-left {{
      animation: tulipSwayLeft 5.5s ease-in-out infinite alternate;
    }}
    .sway-right {{
      animation: tulipSwayRight 4.8s ease-in-out infinite alternate;
    }}
    .sway-soft {{
      animation: tulipSwaySoft 6.4s ease-in-out infinite alternate;
    }}

    @keyframes tulipSwayLeft {{
      0% {{ transform: rotate(0deg); }}
      50% {{ transform: rotate(-3deg) translateY(-2px); }}
      100% {{ transform: rotate(2.4deg); }}
    }}

    @keyframes tulipSwayRight {{
      0% {{ transform: rotate(-2deg); }}
      50% {{ transform: rotate(3.4deg) translateY(-3px); }}
      100% {{ transform: rotate(0deg); }}
    }}

    @keyframes tulipSwaySoft {{
      0% {{ transform: rotate(1.4deg); }}
      50% {{ transform: rotate(-2.2deg) translateY(-1px); }}
      100% {{ transform: rotate(2.6deg); }}
    }}

    .tulip-garden-container.boosted .tulip-stem {{
      transform: translateY(-35px) scale(1.1);
      filter: drop-shadow(0 0 20px rgba(244, 114, 182, 0.65)) brightness(1.1);
    }}

    /* =====================================================================
       SCREEN 2: TẤM THIỆP YÊU THƯƠNG (NẰM ĐÈ LÊN TRÊN VƯỜN HOA - z-index: 20)
       Căn giữa màn hình tự nhiên, thanh lịch, nổi bật trên nền hoa phía sau
       ===================================================================== */
    .card-container {{
      width: 100%;
      max-width: 500px;
      max-height: calc(100vh - 65px);
      position: relative;
      margin: auto;
      perspective: 1200px;
      z-index: 20; /* TẤM THIỆP NẰM ĐÈ LÊN TRÊN VƯỜN HOA */
      display: flex;
      justify-content: center;
      align-items: center;
    }}

    .love-card {{
      width: 100%;
      max-height: calc(100vh - 65px);
      background: var(--card-bg);
      backdrop-filter: blur(25px);
      -webkit-backdrop-filter: blur(25px);
      border: 1px solid var(--card-border);
      border-radius: 24px;
      padding: clamp(16px, 2.5vh, 26px) clamp(18px, 4vw, 32px);
      box-shadow: var(--card-shadow);
      position: relative;
      text-align: center;
      overflow: hidden;
      box-sizing: border-box;
      transform-style: preserve-3d;
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease;
      display: flex;
      flex-direction: column;
      justify-content: center;
      z-index: 21;
    }}

    .love-card:hover {{
      box-shadow: 0 20px 45px rgba(0, 0, 0, 0.16), 
                  0 0 35px rgba(255, 255, 255, 0.95), 
                  0 30px 70px -10px rgba(180, 80, 100, 0.22);
    }}

    .love-card::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: radial-gradient(circle at 85% 15%, rgba(254, 215, 226, 0.25) 0%, transparent 60%),
                  radial-gradient(circle at 15% 85%, rgba(240, 253, 244, 0.3) 0%, transparent 60%);
      pointer-events: none;
      z-index: 0;
    }}

    .card-border-inner {{
      position: absolute;
      top: 10px;
      left: 10px;
      right: 10px;
      bottom: 10px;
      border: 1px solid rgba(220, 175, 185, 0.35);
      border-radius: 18px;
      pointer-events: none;
      z-index: 1;
    }}

    .card-content {{
      position: relative;
      z-index: 2;
    }}

    .card-header-icon {{
      width: 38px;
      height: 38px;
      margin: 0 auto 5px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(254, 226, 226, 0.75);
      border-radius: 50%;
      border: 1px solid rgba(252, 165, 165, 0.5);
      box-shadow: 0 4px 12px rgba(225, 29, 72, 0.1);
      animation: floatAura 6s ease-in-out infinite alternate;
      overflow: hidden;
    }}

    .card-header-icon img {{
      width: 24px;
      height: 24px;
      object-fit: contain;
    }}

    .card-salutation {{
      font-family: 'Cormorant Garamond', serif;
      font-style: italic;
      font-size: 1.15rem;
      color: #8c3b47;
      margin-bottom: 3px;
      letter-spacing: 0.04em;
    }}

    .card-title {{
      font-family: 'Playfair Display', serif;
      font-size: clamp(1.25rem, 2.7vw, 1.5rem);
      font-weight: 700;
      color: #381b20;
      line-height: 1.25;
      margin-bottom: 9px;
      letter-spacing: -0.01em;
    }}

    .card-divider {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      margin: 7px 0 9px;
      color: #e5989b;
    }}

    .card-divider span {{
      width: 36px;
      height: 1px;
      background: linear-gradient(90deg, transparent, #d98880, transparent);
    }}

    .card-poem {{
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(0.95rem, 1.85vw, 1.1rem);
      line-height: 1.45;
      color: #55272e;
      text-align: center;
      margin-bottom: 7px;
      padding: 0 4px;
    }}

    .card-poem .highlight-verse {{
      font-style: italic;
      font-size: 1.14em;
      color: #9f1239;
      display: block;
      margin-bottom: 3px;
      font-weight: 600;
      line-height: 1.38;
    }}

    .card-wish {{
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(0.81rem, 1.48vw, 0.9rem);
      line-height: 1.48;
      color: #633e44;
      font-weight: 300;
      margin-bottom: 7px;
      padding: 0 4px;
    }}

    .card-wish strong {{
      font-weight: 500;
      color: #881337;
    }}

    .card-closing {{
      font-family: 'Cormorant Garamond', serif;
      font-style: italic;
      font-size: 1.16rem;
      color: #9f1239;
      font-weight: 600;
      margin-top: 3px;
      margin-bottom: 11px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
    }}

    .card-closing .heart-pulse {{
      display: inline-block;
      color: #e11d48;
      animation: heartbeat 1.5s infinite ease-in-out;
    }}

    @keyframes heartbeat {{
      0%, 100% {{ transform: scale(1); }}
      15% {{ transform: scale(1.3); }}
      30% {{ transform: scale(1); }}
      45% {{ transform: scale(1.22); }}
    }}

    /* Action Buttons in Card */
    .card-actions {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
      margin-top: 2px;
    }}

    .btn-garden {{
      background: linear-gradient(135deg, #e11d48 0%, #be123c 60%, #9f1239 100%);
      color: #ffffff;
      border: none;
      padding: 8px 25px;
      font-size: 0.9rem;
      font-weight: 500;
      font-family: 'Be Vietnam Pro', sans-serif;
      border-radius: 40px;
      cursor: pointer;
      box-shadow: 0 6px 18px -3px rgba(225, 29, 72, 0.42), 0 0 0 1px rgba(255, 255, 255, 0.35) inset;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      display: inline-flex;
      align-items: center;
      gap: 8px;
      letter-spacing: 0.02em;
      position: relative;
      overflow: hidden;
    }}

    .btn-garden::before {{
      content: "";
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: linear-gradient(45deg, transparent 40%, rgba(255, 255, 255, 0.35) 50%, transparent 60%);
      transform: rotate(25deg) translateY(-100%);
      transition: transform 0.75s ease;
    }}

    .btn-garden:hover {{
      transform: translateY(-2px) scale(1.02);
      box-shadow: 0 10px 22px -3px rgba(225, 29, 72, 0.52);
      background: linear-gradient(135deg, #f43f5e 0%, #be123c 60%, #881337 100%);
    }}

    .btn-garden:active {{
      transform: translateY(0) scale(0.98);
    }}

    .btn-replay {{
      background: transparent;
      border: none;
      color: #92535c;
      font-size: 0.78rem;
      cursor: pointer;
      padding: 3px 10px;
      border-radius: 20px;
      transition: all 0.25s ease;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-family: 'Be Vietnam Pro', sans-serif;
    }}

    .btn-replay:hover {{
      color: #611824;
      background: rgba(146, 83, 92, 0.08);
    }}

    /* Animation Utilities */
    @keyframes fadeInDown {{
      from {{ opacity: 0; transform: translateY(-20px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    @keyframes fadeInUp {{
      from {{ opacity: 0; transform: translateY(20px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    @keyframes growFlower {{
      0% {{ transform: scale(0) translateY(120px) rotate(10deg); opacity: 0; }}
      70% {{ transform: scale(1.06) translateY(-8px) rotate(-3deg); opacity: 1; }}
      100% {{ transform: scale(1) translateY(0) rotate(0deg); opacity: 1; }}
    }}

    /* Responsive adjustments for Mobile */
    @media (max-width: 640px) {{
      .top-bar {{
        padding: 10px 14px;
      }}
      .brand-tag {{
        font-size: 0.88rem;
        padding: 4px 10px;
      }}
      .audio-btn {{
        padding: 6px 12px;
      }}
      #screen2 {{
        padding: 14px 12px;
      }}
      .love-card {{
        padding: 15px 12px 12px;
        border-radius: 20px;
      }}
      .card-border-inner {{
        top: 6px;
        left: 6px;
        right: 6px;
        bottom: 6px;
      }}
      .card-title {{
        font-size: 1.22rem;
        margin-bottom: 6px;
      }}
      .card-poem {{
        margin-bottom: 5px;
      }}
      .card-wish {{
        font-size: 0.78rem;
        line-height: 1.42;
        margin-bottom: 5px;
      }}
      .tulip-watercolor-img {{
        width: 180px;
      }}
      .tulip-garden-container {{
        height: 46vh;
        min-height: 320px;
      }}
    }}
  </style>
</head>
<body>

  <!-- Audio Element: Bài hát "Một Nhành Hoa" -->
  <audio id="bgMusic" loop preload="auto" src="mot-nhanh-hoa.mp3"></audio>

  <!-- Morning Sunlight & Vignette Overlay -->
  <div class="vignette-overlay"></div>

  <!-- Soft Atmospheric Light Leaks -->
  <div class="light-leak leak-1"></div>
  <div class="light-leak leak-2"></div>
  <div class="light-leak leak-3"></div>

  <!-- Ambient Particle Canvas (Sparkles & Falling Petals) -->
  <canvas id="ambientCanvas"></canvas>

  <!-- Top Header Bar -->
  <header class="top-bar">
    <div class="brand-tag">Dành bạn, cả một vườn thương.</div>
    <button class="audio-btn" id="audioToggleBtn" title="Bật/Tắt nhạc Một Nhành Hoa" aria-label="Bật hoặc tắt nhạc nền">
      <div class="audio-bars">
        <span></span>
        <span></span>
        <span></span>
      </div>
      <span class="label" id="audioLabel">♫ Một Nhành Hoa</span>
    </button>
  </header>

  <!-- ==================== MÀN HÌNH 1: BÔNG HOA TULIP VÀ LỜI MỜI ==================== -->
  <main class="app-screen" id="screen1">
    <div class="hero-content">
      <h1 class="hero-title">Từ một bông hoa nhỏ...</h1>
      <p class="hero-subtitle">
        Chạm vào hoa, một điều dịu dàng đang chờ bạn <span class="sparkle-icon">✦</span>
      </p>

      <!-- Tâm điểm cành hoa Tulip trong suốt không nền -->
      <div class="flower-wrapper" id="roseFlower" role="button" tabindex="0" aria-label="Chạm vào đóa hoa tulip hồng để nhận quà 20/10">
        <div class="flower-glow"></div>

        <img class="tulip-watercolor-img" id="mainTulipImg" src="{tulip_b64}" alt="Đóa hoa Tulip hồng phấn màu nước thanh nhã" />

        <!-- Hiệu ứng đốm sáng lấp lánh bao quanh hoa tulip -->
        <svg class="tulip-sparkles-overlay" viewBox="0 0 320 500" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M 60 110 Q 60 122 48 122 Q 60 122 60 134 Q 60 122 72 122 Q 60 122 60 110 Z" fill="#fde047" opacity="0.9">
            <animate attributeName="opacity" values="0.3;1;0.3" dur="2.8s" repeatCount="indefinite" />
            <animateTransform attributeName="transform" type="rotate" from="0 60 122" to="360 60 122" dur="10s" repeatCount="indefinite"/>
          </path>
          <path d="M 270 140 Q 270 152 258 152 Q 270 152 270 164 Q 270 152 282 152 Q 270 152 270 140 Z" fill="#fbbf24" opacity="0.85">
            <animate attributeName="opacity" values="0.8;0.2;0.8" dur="3.2s" repeatCount="indefinite" />
            <animateTransform attributeName="transform" type="rotate" from="0 270 152" to="-360 270 152" dur="12s" repeatCount="indefinite"/>
          </path>
          <path d="M 180 40 Q 180 50 170 50 Q 180 50 180 60 Q 180 50 190 50 Q 180 50 180 40 Z" fill="#fef08a" opacity="0.95">
            <animate attributeName="opacity" values="0.4;1;0.4" dur="2.4s" repeatCount="indefinite" />
          </path>
          <circle cx="90" cy="80" r="3" fill="#fde047" opacity="0.75" />
          <circle cx="240" cy="70" r="2.5" fill="#fef08a" opacity="0.8" />
          <circle cx="50" cy="220" r="2.5" fill="#fde68a" opacity="0.65" />
          <circle cx="280" cy="230" r="3.2" fill="#fde047" opacity="0.75" />
          <circle cx="100" cy="360" r="2" fill="#fef08a" opacity="0.5" />
          <circle cx="220" cy="370" r="2.2" fill="#fde68a" opacity="0.6" />
        </svg>
      </div>

      <!-- Nút gợi ý chạm -->
      <div class="tap-hint" id="tapHintBtn">
        <span class="tap-hint-hand">✨</span>
        <span>Chạm nhẹ vào đóa hoa</span>
      </div>
    </div>
  </main>

  <!-- ==================== MÀN HÌNH 2: TẤM THIỆP YÊU THƯƠNG ==================== -->
  <main class="app-screen" id="screen2">
    <!-- TẤM THIỆP ĐƯỢC CĂN GIỮA MÀN HÌNH TỰ NHIÊN, NẰM ĐÈ LÊN TRÊN VƯỜN HOA (z-index: 20) -->
    <div class="card-container">
      <article class="love-card">
        <div class="card-border-inner"></div>
        <div class="card-content">
          
          <!-- Mini Tulip Icon -->
          <div class="card-header-icon">
            <img src="{tulip_b64}" alt="Mini Tulip Icon" />
          </div>

          <p class="card-salutation">Gửi bạn thương mến,</p>
          <h2 class="card-title">Mong những điều đẹp đẽ<br>luôn nở bên bạn.</h2>

          <div class="card-divider">
            <span></span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="#e11d48">
              <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
            </svg>
            <span></span>
          </div>

          <div class="card-poem">
            <span class="highlight-verse">"Một bông hoa có thể làm một ngày thêm đẹp.<br>Còn bạn, làm thế giới này dịu dàng hơn."</span>
          </div>

          <p class="card-wish">
            Nhân ngày <strong>20/10</strong>, chúc bạn luôn được yêu thương, trân trọng và có thật nhiều niềm vui. Mong bạn đủ bình yên để tận hưởng những điều nhỏ bé, đủ tự tin để theo đuổi những điều mình yêu.
          </p>

          <p class="card-wish" style="margin-bottom: 5px;">
            Hôm nay và cả những ngày sau,<br>
            <strong>hãy cứ rạng rỡ theo cách của riêng mình nhé.</strong>
          </p>

          <p class="card-closing">
            Gửi bạn thật nhiều thương mến <span class="heart-pulse">♡</span>
          </p>

          <div class="card-actions">
            <!-- Nút tương tác: Ngắm thêm hoa -->
            <button class="btn-garden" id="btnBloomGarden">
              <span>Ngắm thêm hoa</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/>
              </svg>
            </button>
            <button class="btn-replay" id="btnBackToFlower">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="15 18 9 12 15 6"></polyline>
              </svg>
              <span>Về lại bông hoa nhỏ</span>
            </button>
          </div>

        </div>
      </article>
    </div>
  </main>

  <!-- =====================================================================
       CÁNH ĐỒNG HOA TULIP NỀN: NẰM HOÀN TOÀN Ở LỚP NỀN PHÍA SAU (z-index: 2)
       Chiếm 45% - 50% màn hình, đan xen khít nhau lấp ló 2 bên và dưới chân thiệp
       ===================================================================== -->
  <div class="tulip-garden-container" id="tulipGarden">
    <div class="garden-ground-mist"></div>
    <div class="tulip-layer deep-back" id="tulipLayerDeep"></div>
    <div class="tulip-layer back" id="tulipLayerBack"></div>
    <div class="tulip-layer mid" id="tulipLayerMid"></div>
    <div class="tulip-layer front" id="tulipLayerFront"></div>
  </div>

  <script>
    const tulipImgSrc = "{tulip_b64}";

    /* =====================================================================
       1. QUẢN LÝ PHÁT NHẠC "MỘT NHÀNH HOA" & DỰ PHÒNG SYNTHESIZER
       ===================================================================== */
    const bgMusic = document.getElementById('bgMusic');
    const audioToggleBtn = document.getElementById('audioToggleBtn');
    const audioLabel = document.getElementById('audioLabel');

    let isMusicPlaying = false;
    let useSynthFallback = false;
    let audioCtx = null;
    let melodyTimer = null;
    let noteIndex = 0;

    function updateAudioButtonState(playing) {{
      isMusicPlaying = playing;
      if (playing) {{
        audioToggleBtn.classList.add('playing');
        audioLabel.textContent = 'Một Nhành Hoa ♫';
      }} else {{
        audioToggleBtn.classList.remove('playing');
        audioLabel.textContent = '♫ Một Nhành Hoa';
      }}
    }}

    // Phát bài hát "Một Nhành Hoa"
    function playMusic() {{
      if (!useSynthFallback) {{
        const playPromise = bgMusic.play();
        if (playPromise !== undefined) {{
          playPromise.then(() => {{
            updateAudioButtonState(true);
          }}).catch((err) => {{
            console.info('Chưa tìm thấy file mot-nhanh-hoa.mp3 hoặc trình duyệt chặn, tự động bật giai điệu dự phòng Web Audio:', err);
            useSynthFallback = true;
            startSynthMusic();
          }});
        }}
      }} else {{
        startSynthMusic();
      }}
    }}

    // Tạm dừng nhạc
    function pauseMusic() {{
      if (!useSynthFallback) {{
        bgMusic.pause();
      }} else {{
        stopSynthMusic();
      }}
      updateAudioButtonState(false);
    }}

    // Chuyển đổi Bật / Tắt nhạc khi nhấn nút góc phải
    function toggleMusic() {{
      if (isMusicPlaying) {{
        pauseMusic();
      }} else {{
        playMusic();
      }}
    }}

    // Lắng nghe các sự kiện native của thẻ audio
    bgMusic.addEventListener('play', () => updateAudioButtonState(true));
    bgMusic.addEventListener('pause', () => updateAudioButtonState(false));
    bgMusic.addEventListener('error', () => {{
      // Khi file mp3 chưa tồn tại ở local, tự động chuyển sang synth fallback
      useSynthFallback = true;
      if (isMusicPlaying) {{
        startSynthMusic();
      }}
    }});

    /* =====================================================================
       DỰ PHÒNG: WEB AUDIO API KHI CHƯA CÓ FILE MP3 LOCAL
       ===================================================================== */
    function getAudioContext() {{
      if (!audioCtx) {{
        const AudioContextClass = window.AudioContext || window.webkitAudioContext;
        audioCtx = new AudioContextClass();
      }}
      if (audioCtx.state === 'suspended') {{
        audioCtx.resume();
      }}
      return audioCtx;
    }}

    const melody = [
      {{ note: 261.63, dur: 0.6 }}, // C4
      {{ note: 329.63, dur: 0.6 }}, // E4
      {{ note: 392.00, dur: 0.8 }}, // G4
      {{ note: 523.25, dur: 1.2 }}, // C5
      {{ note: 440.00, dur: 0.6 }}, // A4
      {{ note: 392.00, dur: 0.6 }}, // G4
      {{ note: 329.63, dur: 1.0 }}, // E4
      {{ note: 293.66, dur: 0.6 }}, // D4
      {{ note: 329.63, dur: 0.6 }}, // E4
      {{ note: 392.00, dur: 1.2 }}, // G4
      {{ note: 523.25, dur: 0.8 }}, // C5
      {{ note: 587.33, dur: 0.8 }}, // D5
      {{ note: 659.25, dur: 1.6 }}, // E5
      {{ note: 587.33, dur: 0.6 }}, // D5
      {{ note: 523.25, dur: 0.8 }}, // C5
      {{ note: 440.00, dur: 1.2 }}  // A4
    ];

    function playPianoTone(freq, duration = 1.0, gainLevel = 0.12) {{
      const ctx = getAudioContext();
      if (!ctx) return;

      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      const filter = ctx.createBiquadFilter();

      osc.type = 'triangle';
      osc.frequency.setValueAtTime(freq, ctx.currentTime);

      filter.type = 'lowpass';
      filter.frequency.setValueAtTime(1400, ctx.currentTime);
      filter.frequency.exponentialRampToValueAtTime(400, ctx.currentTime + duration);

      const now = ctx.currentTime;
      gain.gain.setValueAtTime(0.0001, now);
      gain.gain.linearRampToValueAtTime(gainLevel, now + 0.04);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);

      osc.connect(filter);
      filter.connect(gain);
      gain.connect(ctx.destination);

      osc.start(now);
      osc.stop(now + duration);
    }}

    function scheduleNextNote() {{
      if (!isMusicPlaying || !useSynthFallback) return;
      const current = melody[noteIndex];
      playPianoTone(current.note, current.dur * 1.8, 0.11);

      if (noteIndex % 4 === 0) {{
        playPianoTone(current.note / 2, 2.0, 0.06);
      }}

      noteIndex = (noteIndex + 1) % melody.length;
      melodyTimer = setTimeout(scheduleNextNote, current.dur * 1000);
    }}

    function startSynthMusic() {{
      getAudioContext();
      updateAudioButtonState(true);
      if (melodyTimer) clearTimeout(melodyTimer);
      scheduleNextNote();
    }}

    function stopSynthMusic() {{
      if (melodyTimer) clearTimeout(melodyTimer);
      updateAudioButtonState(false);
    }}

    // Hiệu ứng âm thanh chime khi chạm hoa
    function playChimeEffect() {{
      const notes = [523.25, 659.25, 783.99, 1046.50, 1318.51, 1567.98];
      notes.forEach((freq, idx) => {{
        setTimeout(() => {{
          playPianoTone(freq, 1.4, 0.15);
        }}, idx * 75);
      }});
    }}

    // Hiệu ứng âm thanh bung nở hoa
    function playGardenBloomSound() {{
      const notes = [392.00, 523.25, 659.25, 783.99, 1046.50, 1174.66, 1318.51, 1567.98, 2093.00];
      notes.forEach((freq, idx) => {{
        setTimeout(() => {{
          playPianoTone(freq, 1.6, 0.14);
        }}, idx * 60);
      }});
    }}

    /* =====================================================================
       2. CANVAS HIỆU ỨNG NỀN: HẠT BỤI VÀNG & CÁNH HOA TULIP RƠI
       ===================================================================== */
    const canvas = document.getElementById('ambientCanvas');
    const ctx = canvas.getContext('2d');
    let width = window.innerWidth;
    let height = window.innerHeight;

    function resizeCanvas() {{
      width = window.innerWidth;
      height = window.innerHeight;
      canvas.width = width;
      canvas.height = height;
    }}
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    const particles = [];
    const MAX_PARTICLES = 36;

    class Particle {{
      constructor(isPetal = false) {{
        this.reset(isPetal);
      }}

      reset(isPetal) {{
        this.x = Math.random() * width;
        this.y = Math.random() * -height * 0.5;
        this.isPetal = isPetal !== undefined ? isPetal : Math.random() > 0.45;
        
        if (this.isPetal) {{
          this.size = 9 + Math.random() * 10;
          this.speedY = 0.9 + Math.random() * 1.5;
          this.speedX = (Math.random() - 0.5) * 1.2;
          this.rot = Math.random() * Math.PI * 2;
          this.rotSpeed = (Math.random() - 0.5) * 0.03;
          this.flip = Math.random() * Math.PI;
          this.flipSpeed = 0.02 + Math.random() * 0.03;
          this.color = Math.random() > 0.5 ? '#f472b6' : '#fda4af';
          this.opacity = 0.5 + Math.random() * 0.4;
        }} else {{
          this.size = 1.4 + Math.random() * 2.8;
          this.speedY = 0.3 + Math.random() * 0.7;
          this.speedX = (Math.random() - 0.5) * 0.5;
          this.opacity = 0.3 + Math.random() * 0.6;
          this.pulse = Math.random() * Math.PI * 2;
        }}
      }}

      update() {{
        this.y += this.speedY;
        this.x += this.speedX + Math.sin(this.y * 0.01) * 0.5;

        if (this.isPetal) {{
          this.rot += this.rotSpeed;
          this.flip += this.flipSpeed;
        }} else {{
          this.pulse += 0.05;
        }}

        if (this.y > height + 40 || this.x < -40 || this.x > width + 40) {{
          this.reset(this.isPetal);
          this.y = -20;
        }}
      }}

      draw() {{
        ctx.save();
        if (this.isPetal) {{
          ctx.translate(this.x, this.y);
          ctx.rotate(this.rot);
          ctx.scale(Math.cos(this.flip), 1);
          ctx.beginPath();
          ctx.moveTo(0, 0);
          ctx.bezierCurveTo(this.size, -this.size * 0.8, this.size * 1.2, this.size * 0.8, 0, this.size * 1.4);
          ctx.bezierCurveTo(-this.size * 1.2, this.size * 0.8, -this.size, -this.size * 0.8, 0, 0);
          ctx.fillStyle = this.color;
          ctx.globalAlpha = this.opacity;
          ctx.shadowColor = 'rgba(244, 114, 182, 0.4)';
          ctx.shadowBlur = 6;
          ctx.fill();
        }} else {{
          ctx.beginPath();
          ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
          ctx.fillStyle = '#fde047';
          ctx.globalAlpha = this.opacity * (0.6 + Math.sin(this.pulse) * 0.4);
          ctx.shadowColor = '#fef08a';
          ctx.shadowBlur = 8;
          ctx.fill();
        }}
        ctx.restore();
      }}
    }}

    for (let i = 0; i < MAX_PARTICLES; i++) {{
      const p = new Particle();
      p.y = Math.random() * height;
      particles.push(p);
    }}

    function animateParticles() {{
      ctx.clearRect(0, 0, width, height);
      for (let i = 0; i < particles.length; i++) {{
        particles[i].update();
        particles[i].draw();
      }}
      requestAnimationFrame(animateParticles);
    }}
    animateParticles();

    /* =====================================================================
       3. KHỞI TẠO CÁNH ĐỒNG HOA TULIP DÀY ĐẶC CHIẾM NỬA MÀN HÌNH (4 TẦNG LỚP)
       ===================================================================== */
    const tulipColorFilters = [
      'none', // Hồng phấn tự nhiên
      'hue-rotate(-18deg) saturate(1.4) brightness(0.95)', // Đỏ thắm
      'hue-rotate(-42deg) saturate(1.3) brightness(1.05)', // Cam đào ấm áp
      'hue-rotate(-75deg) saturate(1.2) brightness(1.15)', // Vàng kem hoàng gia
      'hue-rotate(42deg) saturate(1.1) brightness(1.02)'    // Tím pastel lavender
    ];

    function buildWatercolorTulipGarden() {{
      const deepLayer = document.getElementById('tulipLayerDeep');
      const backLayer = document.getElementById('tulipLayerBack');
      const midLayer = document.getElementById('tulipLayerMid');
      const frontLayer = document.getElementById('tulipLayerFront');
      if (!deepLayer || !backLayer || !midLayer || !frontLayer) return;

      deepLayer.innerHTML = '';
      backLayer.innerHTML = '';
      midLayer.innerHTML = '';
      frontLayer.innerHTML = '';

      const screenW = window.innerWidth;
      const gardenH = document.getElementById('tulipGarden').clientHeight || 420;

      const countDeep = Math.max(16, Math.floor(screenW / 65));
      const countBack = Math.max(18, Math.floor(screenW / 55));
      const countMid = Math.max(20, Math.floor(screenW / 48));
      const countFront = Math.max(14, Math.floor(screenW / 70));

      const swayClasses = ['sway-left', 'sway-right', 'sway-soft'];

      function createTulipElement(heightPx, swayClass, delaySec, isFlipped, rotDeg, leftPercent, colorFilter) {{
        const stem = document.createElement('div');
        stem.className = `tulip-stem ${{swayClass}}`;
        stem.style.height = `${{heightPx}}px`;
        stem.style.animationDelay = `${{delaySec}}s`;
        stem.style.left = `${{leftPercent}}%`;

        const flipFactor = isFlipped ? -1 : 1;
        stem.style.transform = `scaleX(${{flipFactor}}) rotate(${{rotDeg}}deg)`;

        const img = document.createElement('img');
        img.className = 'tulip-flora-img';
        img.src = tulipImgSrc;
        img.alt = 'Tulip Flora';
        if (colorFilter && colorFilter !== 'none') {{
          img.style.filter = colorFilter;
        }}

        stem.appendChild(img);
        return stem;
      }}

      // 1. Tầng sâu nhất (Deep Back)
      for (let i = 0; i < countDeep; i++) {{
        const baseH = gardenH * 0.94;
        const height = baseH + (Math.random() - 0.5) * 40;
        const sway = swayClasses[i % swayClasses.length];
        const delay = (Math.random() * -5).toFixed(1);
        const isFlipped = i % 2 === 1;
        const rot = (Math.random() - 0.5) * 8;
        const left = (i / countDeep * 100) + (Math.random() - 0.5) * 4;
        const color = tulipColorFilters[i % tulipColorFilters.length];

        deepLayer.appendChild(createTulipElement(height, sway, delay, isFlipped, rot, left, color));
      }}

      // 2. Tầng sau (Back)
      for (let i = 0; i < countBack; i++) {{
        const baseH = gardenH * 0.88;
        const height = baseH + (Math.random() - 0.5) * 35;
        const sway = swayClasses[(i + 1) % swayClasses.length];
        const delay = (Math.random() * -6).toFixed(1);
        const isFlipped = i % 2 === 0;
        const rot = (Math.random() - 0.5) * 7;
        const left = ((i + 0.5) / countBack * 100) + (Math.random() - 0.5) * 5;
        const color = tulipColorFilters[(i * 2 + 1) % tulipColorFilters.length];

        backLayer.appendChild(createTulipElement(height, sway, delay, isFlipped, rot, left, color));
      }}

      // 3. Tầng giữa (Mid)
      for (let i = 0; i < countMid; i++) {{
        const baseH = gardenH * 0.78;
        const height = baseH + (Math.random() - 0.5) * 30;
        const sway = swayClasses[(i + 2) % swayClasses.length];
        const delay = (Math.random() * -5.5).toFixed(1);
        const isFlipped = (i * 3) % 2 === 1;
        const rot = (Math.random() - 0.5) * 6;
        const left = (i / countMid * 100) + (Math.random() - 0.5) * 4;
        const color = tulipColorFilters[(i * 3 + 2) % tulipColorFilters.length];

        midLayer.appendChild(createTulipElement(height, sway, delay, isFlipped, rot, left, color));
      }}

      // 4. Tầng trước (Front)
      for (let i = 0; i < countFront; i++) {{
        const baseH = gardenH * 0.65;
        const height = baseH + (Math.random() - 0.5) * 25;
        const sway = swayClasses[i % swayClasses.length];
        const delay = (Math.random() * -4).toFixed(1);
        const isFlipped = i % 2 === 0;
        const rot = (Math.random() - 0.5) * 5;
        const left = ((i + 0.3) / countFront * 100) + (Math.random() - 0.5) * 4;
        const color = tulipColorFilters[(i * 4) % tulipColorFilters.length];

        frontLayer.appendChild(createTulipElement(height, sway, delay, isFlipped, rot, left, color));
      }}
    }}

    buildWatercolorTulipGarden();
    window.addEventListener('resize', buildWatercolorTulipGarden);

    /* =====================================================================
       4. CHUYỂN MÀN HÌNH & HIỆU ỨNG TƯƠNG TÁC
       ===================================================================== */
    const screen1 = document.getElementById('screen1');
    const screen2 = document.getElementById('screen2');
    const roseFlower = document.getElementById('roseFlower');
    const tapHintBtn = document.getElementById('tapHintBtn');
    const btnBloomGarden = document.getElementById('btnBloomGarden');
    const btnBackToFlower = document.getElementById('btnBackToFlower');
    const tulipGarden = document.getElementById('tulipGarden');

    function transitionToScreen2() {{
      // Tự động kích hoạt phát nhạc "Một Nhành Hoa" khi chạm hoa mở thiệp
      playMusic();

      playChimeEffect();

      if (typeof confetti === 'function') {{
        const defaults = {{
          origin: {{ y: 0.6 }},
          colors: ['#f472b6', '#fda4af', '#fef08a', '#fb7185', '#c084fc', '#ffffff']
        }};

        confetti({{
          ...defaults,
          particleCount: 50,
          spread: 75,
          shapes: ['circle']
        }});

        setTimeout(() => {{
          confetti({{
            ...defaults,
            particleCount: 40,
            angle: 60,
            spread: 55,
            origin: {{ x: 0.15, y: 0.65 }}
          }});
          confetti({{
            ...defaults,
            particleCount: 40,
            angle: 120,
            spread: 55,
            origin: {{ x: 0.85, y: 0.65 }}
          }});
        }}, 220);
      }}

      screen1.classList.add('hide');
      setTimeout(() => {{
        screen2.classList.add('show');
        tulipGarden.classList.add('visible');
      }}, 500);
    }}

    function transitionToScreen1() {{
      screen2.classList.remove('show');
      tulipGarden.classList.remove('visible');
      tulipGarden.classList.remove('boosted');
      setTimeout(() => {{
        screen1.classList.remove('hide');
      }}, 400);
    }}

    roseFlower.addEventListener('click', transitionToScreen2);
    tapHintBtn.addEventListener('click', transitionToScreen2);
    btnBackToFlower.addEventListener('click', transitionToScreen1);
    audioToggleBtn.addEventListener('click', toggleMusic);

    roseFlower.addEventListener('keydown', (e) => {{
      if (e.key === 'Enter' || e.key === ' ') {{
        e.preventDefault();
        transitionToScreen2();
      }}
    }});

    /* =====================================================================
       5. SỰ KIỆN NÚT "NGẮM THÊM HOA": CÁNH ĐỒNG BÙNG NỞ RỰC RỠ & PHÁO HOA
       ===================================================================== */
    btnBloomGarden.addEventListener('click', () => {{
      playGardenBloomSound();
      tulipGarden.classList.add('boosted');

      const frontLayer = document.getElementById('tulipLayerFront');
      if (frontLayer) {{
        const gardenH = document.getElementById('tulipGarden').clientHeight || 420;
        for (let i = 0; i < 6; i++) {{
          const freshStem = document.createElement('div');
          freshStem.className = 'tulip-stem sway-soft';
          freshStem.style.height = `${{gardenH * 0.72 + (Math.random() - 0.5) * 30}}px`;
          freshStem.style.left = `${{(i / 5) * 88 + 6}}%`;
          freshStem.style.transform = `scaleX(${{i % 2 === 0 ? 1 : -1}}) rotate(${{(Math.random() - 0.5) * 8}}deg)`;
          freshStem.style.animation = 'growFlower 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards';

          const img = document.createElement('img');
          img.className = 'tulip-flora-img';
          img.src = tulipImgSrc;
          img.alt = 'Fresh Blooming Tulip';
          img.style.filter = tulipColorFilters[i % tulipColorFilters.length];

          freshStem.appendChild(img);
          frontLayer.appendChild(freshStem);
        }}
      }}

      if (typeof confetti === 'function') {{
        const duration = 4.0 * 1000;
        const end = Date.now() + duration;

        (function frame() {{
          confetti({{
            particleCount: 7,
            angle: 60,
            spread: 65,
            origin: {{ x: 0.05, y: 0.85 }},
            colors: ['#f472b6', '#fda4af', '#fde047', '#fb923c', '#c084fc', '#ffffff']
          }});
          confetti({{
            particleCount: 7,
            angle: 120,
            spread: 65,
            origin: {{ x: 0.95, y: 0.85 }},
            colors: ['#f472b6', '#fda4af', '#fde047', '#fb923c', '#c084fc', '#ffffff']
          }});

          if (Date.now() < end) {{
            requestAnimationFrame(frame);
          }}
        }})();

        setTimeout(() => {{
          confetti({{
            particleCount: 90,
            spread: 110,
            origin: {{ y: 0.45 }},
            colors: ['#f472b6', '#fda4af', '#fde047', '#c084fc', '#ffffff']
          }});
        }}, 500);

        setTimeout(() => {{
          confetti({{
            particleCount: 65,
            spread: 90,
            origin: {{ y: 0.32 }},
            colors: ['#fbbf24', '#f472b6', '#38bdf8', '#a855f7']
          }});
        }}, 1200);
      }}
    }});
  </script>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Updated index.html successfully with Mot Nhanh Hoa audio integration and auto-fallback!")
