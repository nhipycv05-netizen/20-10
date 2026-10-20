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
      --card-bg: rgba(255, 255, 255, 0.94);
      --card-border: rgba(255, 255, 255, 0.95);
      --card-shadow: 0 25px 60px -12px rgba(190, 75, 100, 0.16), 0 10px 28px -6px rgba(0, 0, 0, 0.05), 0 0 30px rgba(255, 255, 255, 0.9);
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
      /* Nền gradient chuyển sắc nhẹ nhàng, thanh lịch và trong trẻo: Tone hồng pastel phớt trắng & xanh da trời dịu nhẹ */
      background: linear-gradient(
        160deg,
        #eef6fc 0%,
        #e5f1fb 22%,
        #fdf8fa 48%,
        #fcf0f4 75%,
        #fbe9ef 100%
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
      background: radial-gradient(ellipse at 85% 10%, rgba(255, 253, 240, 0.7) 0%, transparent 55%),
                  radial-gradient(circle at 50% 45%, transparent 60%, rgba(220, 238, 250, 0.25) 90%, rgba(248, 225, 235, 0.3) 100%);
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
      top: -10%;
      left: 10%;
      width: 480px;
      height: 480px;
      background: radial-gradient(circle, rgba(254, 250, 236, 0.8) 0%, rgba(224, 242, 254, 0) 70%);
    }}

    .leak-2 {{
      bottom: -10%;
      right: 15%;
      width: 500px;
      height: 500px;
      background: radial-gradient(circle, rgba(253, 226, 236, 0.55) 0%, rgba(255, 255, 255, 0) 70%);
      animation-delay: -6s;
    }}

    .leak-3 {{
      top: 40%;
      left: 20%;
      width: 400px;
      height: 400px;
      background: radial-gradient(circle, rgba(224, 242, 254, 0.45) 0%, rgba(255, 255, 255, 0) 70%);
      animation-delay: -12s;
    }}

    @keyframes floatAura {{
      0% {{ transform: translate(0, 0) scale(1); }}
      50% {{ transform: translate(25px, -20px) scale(1.08); }}
      100% {{ transform: translate(-20px, 16px) scale(0.96); }}
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
      background: rgba(255, 255, 255, 0.68);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      padding: 6px 16px;
      border-radius: 30px;
      border: 1px solid rgba(255, 255, 255, 0.88);
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
      pointer-events: auto;
      transition: all 0.3s ease;
    }}

    .brand-tag:hover {{
      background: rgba(255, 255, 255, 0.92);
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
      transition: transform 1.1s cubic-bezier(0.22, 1, 0.36, 1), 
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
      transform: translateY(-70px) scale(0.96);
      pointer-events: none;
    }}

    #screen2 {{
      opacity: 0;
      transform: translateY(30px) scale(0.98);
      pointer-events: none;
      visibility: hidden;
      z-index: 10;
      padding: 60px 16px 24px;
      transition: transform 1.1s cubic-bezier(0.16, 1, 0.3, 1), 
                  opacity 1.0s cubic-bezier(0.16, 1, 0.3, 1),
                  visibility 0s 1.1s;
    }}

    #screen2.show {{
      opacity: 1;
      transform: translateY(0) scale(1);
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
       SCREEN 2: TẤM THIỆP YÊU THƯƠNG (CĂN CHÍNH GIỮA MÀN HÌNH - CENTERED)
       Tối giản, thanh lịch, sang trọng, bo tròn góc, đổ bóng mềm mại
       ===================================================================== */
    .card-container {{
      width: 100%;
      max-width: 500px;
      position: relative;
      margin: auto;
      perspective: 1200px;
      z-index: 20;
      display: flex;
      justify-content: center;
      align-items: center;
    }}

    .love-card {{
      width: 100%;
      background: var(--card-bg);
      backdrop-filter: blur(28px);
      -webkit-backdrop-filter: blur(28px);
      border: 1px solid var(--card-border);
      border-radius: 28px;
      padding: clamp(18px, 2.8vh, 28px) clamp(20px, 4.5vw, 34px);
      box-shadow: var(--card-shadow);
      position: relative;
      text-align: center;
      overflow: hidden;
      box-sizing: border-box;
      transform-style: preserve-3d;
      transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease;
      display: flex;
      flex-direction: column;
      justify-content: center;
      z-index: 21;
    }}

    .love-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 30px 70px -12px rgba(190, 75, 100, 0.22), 
                  0 12px 35px -6px rgba(0, 0, 0, 0.06), 
                  0 0 35px rgba(255, 255, 255, 0.95);
    }}

    .love-card::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: radial-gradient(circle at 85% 15%, rgba(254, 215, 226, 0.3) 0%, transparent 60%),
                  radial-gradient(circle at 15% 85%, rgba(224, 242, 254, 0.3) 0%, transparent 60%);
      pointer-events: none;
      z-index: 0;
    }}

    .card-border-inner {{
      position: absolute;
      top: 10px;
      left: 10px;
      right: 10px;
      bottom: 10px;
      border: 1px solid rgba(225, 165, 180, 0.32);
      border-radius: 20px;
      pointer-events: none;
      z-index: 1;
    }}

    .card-content {{
      position: relative;
      z-index: 2;
    }}

    .card-header-icon {{
      width: 42px;
      height: 42px;
      margin: 0 auto 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(254, 226, 226, 0.8);
      border-radius: 50%;
      border: 1px solid rgba(252, 165, 165, 0.55);
      box-shadow: 0 4px 14px rgba(225, 29, 72, 0.12);
      animation: floatAura 6s ease-in-out infinite alternate;
      overflow: hidden;
    }}

    .card-header-icon img {{
      width: 26px;
      height: 26px;
      object-fit: contain;
    }}

    .card-salutation {{
      font-family: 'Cormorant Garamond', serif;
      font-style: italic;
      font-size: 1.16rem;
      color: #8c3b47;
      margin-bottom: 3px;
      letter-spacing: 0.04em;
    }}

    .card-title {{
      font-family: 'Playfair Display', serif;
      font-size: clamp(1.28rem, 2.7vw, 1.55rem);
      font-weight: 700;
      color: #381b20;
      line-height: 1.25;
      margin-bottom: 8px;
      letter-spacing: -0.01em;
    }}

    .card-divider {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      margin: 6px 0 9px;
      color: #e5989b;
    }}

    .card-divider span {{
      width: 38px;
      height: 1px;
      background: linear-gradient(90deg, transparent, #d98880, transparent);
    }}

    .card-poem {{
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(0.96rem, 1.85vw, 1.12rem);
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
      font-size: clamp(0.82rem, 1.48vw, 0.91rem);
      line-height: 1.5;
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
      font-size: 1.18rem;
      color: #9f1239;
      font-weight: 600;
      margin-top: 4px;
      margin-bottom: 12px;
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
      gap: 7px;
      margin-top: 2px;
    }}

    .btn-garden {{
      background: linear-gradient(135deg, #e11d48 0%, #be123c 60%, #9f1239 100%);
      color: #ffffff;
      border: none;
      padding: 8px 26px;
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
      box-shadow: 0 10px 24px -3px rgba(225, 29, 72, 0.52);
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
        padding: 55px 12px 16px;
      }}
      .love-card {{
        padding: 16px 14px 14px;
        border-radius: 22px;
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
        line-height: 1.44;
        margin-bottom: 5px;
      }}
      .tulip-watercolor-img {{
        width: 180px;
      }}
    }}

    @media (max-height: 700px) {{
      #screen2 {{
        padding: 50px 12px 10px;
      }}
      .love-card {{
        padding: 12px 16px 10px;
      }}
      .card-header-icon {{
        width: 34px;
        height: 34px;
        margin-bottom: 3px;
      }}
      .card-title {{
        font-size: 1.18rem;
        margin-bottom: 4px;
      }}
      .card-poem {{
        margin-bottom: 4px;
      }}
      .card-wish {{
        font-size: 0.76rem;
        margin-bottom: 4px;
        line-height: 1.38;
      }}
      .card-closing {{
        margin-bottom: 8px;
        font-size: 1.05rem;
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
  <div class="leak-2 light-leak"></div>
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
    <!-- TẤM THIỆP CĂN GIỮA CHÍNH TÂM MÀN HÌNH, NỀN TRONG TRẺO, KHÔNG BỊ VƯỜN HOA CHE KHUẤT -->
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
            <!-- Nút tương tác: Ngắm thêm hoa (bung tỏa mưa cánh hoa & pháo hoa rực rỡ) -->
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

  <script>
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

    // Hiệu ứng âm thanh bung nở hoa ngọt ngào
    function playGardenBloomSound() {{
      const notes = [392.00, 523.25, 659.25, 783.99, 1046.50, 1174.66, 1318.51, 1567.98, 2093.00];
      notes.forEach((freq, idx) => {{
        setTimeout(() => {{
          playPianoTone(freq, 1.6, 0.14);
        }}, idx * 60);
      }});
    }}

    /* =====================================================================
       2. CANVAS HIỆU ỨNG NỀN: CÁNH HOA TỰ NHIÊN RƠI CHẦM CHẬM & BỤI NẮNG
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
    const BASE_PARTICLES = 40;

    class Particle {{
      constructor(isPetal = false, fromBurst = false) {{
        this.reset(isPetal, fromBurst);
      }}

      reset(isPetal, fromBurst = false) {{
        this.x = Math.random() * width;
        this.y = fromBurst ? Math.random() * (height * 0.4) : (Math.random() * -height * 0.5);
        this.isPetal = isPetal !== undefined ? isPetal : Math.random() > 0.4;
        
        if (this.isPetal) {{
          this.size = 8 + Math.random() * 11;
          this.speedY = 0.7 + Math.random() * 1.1; // Cánh hoa rơi chầm chậm tự nhiên
          this.speedX = (Math.random() - 0.5) * 0.9;
          this.rot = Math.random() * Math.PI * 2;
          this.rotSpeed = (Math.random() - 0.5) * 0.025;
          this.flip = Math.random() * Math.PI;
          this.flipSpeed = 0.015 + Math.random() * 0.025;
          // Gam màu cánh hoa hồng pastel phớt đào ngọt ngào
          const palette = ['#f472b6', '#fda4af', '#fb7185', '#fecdd3', '#fbcfe8'];
          this.color = palette[Math.floor(Math.random() * palette.length)];
          this.opacity = 0.55 + Math.random() * 0.35;
        }} else {{
          this.size = 1.2 + Math.random() * 2.5;
          this.speedY = 0.25 + Math.random() * 0.6;
          this.speedX = (Math.random() - 0.5) * 0.4;
          this.opacity = 0.3 + Math.random() * 0.6;
          this.pulse = Math.random() * Math.PI * 2;
        }}
      }}

      update() {{
        this.y += this.speedY;
        this.x += this.speedX + Math.sin(this.y * 0.008) * 0.6;

        if (this.isPetal) {{
          this.rot += this.rotSpeed;
          this.flip += this.flipSpeed;
        }} else {{
          this.pulse += 0.05;
        }}

        if (this.y > height + 40 || this.x < -40 || this.x > width + 40) {{
          this.reset(this.isPetal, false);
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
          ctx.shadowColor = 'rgba(244, 114, 182, 0.35)';
          ctx.shadowBlur = 5;
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

    for (let i = 0; i < BASE_PARTICLES; i++) {{
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

    // Thêm mưa cánh hoa khi bấm "Ngắm thêm hoa"
    function burstFallingPetals() {{
      for (let i = 0; i < 24; i++) {{
        const p = new Particle(true, true);
        p.speedY = 1.0 + Math.random() * 1.4;
        particles.push(p);
      }}
      // Giới hạn số lượng hạt để giữ 60fps mượt mà
      if (particles.length > 90) {{
        particles.splice(0, particles.length - 70);
      }}
    }}

    /* =====================================================================
       3. CHUYỂN MÀN HÌNH & HIỆU ỨNG TƯƠNG TÁC
       ===================================================================== */
    const screen1 = document.getElementById('screen1');
    const screen2 = document.getElementById('screen2');
    const roseFlower = document.getElementById('roseFlower');
    const tapHintBtn = document.getElementById('tapHintBtn');
    const btnBloomGarden = document.getElementById('btnBloomGarden');
    const btnBackToFlower = document.getElementById('btnBackToFlower');

    function transitionToScreen2() {{
      // Tự động kích hoạt phát nhạc "Một Nhành Hoa" khi chạm hoa mở thiệp
      playMusic();
      playChimeEffect();

      if (typeof confetti === 'function') {{
        const defaults = {{
          origin: {{ y: 0.55 }},
          colors: ['#f472b6', '#fda4af', '#fef08a', '#fb7185', '#c084fc', '#ffffff']
        }};

        confetti({{
          ...defaults,
          particleCount: 50,
          spread: 80,
          shapes: ['circle']
        }});

        setTimeout(() => {{
          confetti({{
            ...defaults,
            particleCount: 40,
            angle: 60,
            spread: 60,
            origin: {{ x: 0.15, y: 0.6 }}
          }});
          confetti({{
            ...defaults,
            particleCount: 40,
            angle: 120,
            spread: 60,
            origin: {{ x: 0.85, y: 0.6 }}
          }});
        }}, 220);
      }}

      screen1.classList.add('hide');
      setTimeout(() => {{
        screen2.classList.add('show');
      }}, 450);
    }}

    function transitionToScreen1() {{
      screen2.classList.remove('show');
      setTimeout(() => {{
        screen1.classList.remove('hide');
      }}, 350);
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
       4. SỰ KIỆN NÚT "NGẮM THÊM HOA": MƯA CÁNH HOA BAY LƯỢN & PHÁO HOA
       ===================================================================== */
    btnBloomGarden.addEventListener('click', () => {{
      playGardenBloomSound();
      burstFallingPetals();

      if (typeof confetti === 'function') {{
        const duration = 3.5 * 1000;
        const end = Date.now() + duration;

        (function frame() {{
          confetti({{
            particleCount: 6,
            angle: 60,
            spread: 70,
            origin: {{ x: 0.05, y: 0.8 }},
            colors: ['#f472b6', '#fda4af', '#fde047', '#fb923c', '#c084fc', '#ffffff']
          }});
          confetti({{
            particleCount: 6,
            angle: 120,
            spread: 70,
            origin: {{ x: 0.95, y: 0.8 }},
            colors: ['#f472b6', '#fda4af', '#fde047', '#fb923c', '#c084fc', '#ffffff']
          }});

          if (Date.now() < end) {{
            requestAnimationFrame(frame);
          }}
        }})();

        setTimeout(() => {{
          confetti({{
            particleCount: 80,
            spread: 110,
            origin: {{ y: 0.45 }},
            colors: ['#f472b6', '#fda4af', '#fde047', '#c084fc', '#ffffff']
          }});
        }}, 400);

        setTimeout(() => {{
          confetti({{
            particleCount: 60,
            spread: 90,
            origin: {{ y: 0.35 }},
            colors: ['#fbbf24', '#f472b6', '#38bdf8', '#a855f7']
          }});
        }}, 1000);
      }}
    }});
  </script>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Updated index.html successfully with minimalist elegant Screen 2, centered love card, and removed tulip garden!")
