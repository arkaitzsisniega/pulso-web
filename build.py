#!/usr/bin/env python3
"""Genera la web de PULSO en castellano (index.html) e inglés (en/index.html).

Los textos de los dos idiomas viven aquí, juntos, para que no se separen.
Uso:  python3 build.py   (necesita Pillow solo para leer el tamaño de las imágenes)
"""
from html import escape
from pathlib import Path
from urllib.parse import quote

from PIL import Image

RAIZ = Path(__file__).resolve().parent
DOMINIO = "https://pulso-futsal.com"
# Correo de contacto de PULSO (Zoho, desde el 16/11/2026).
CORREO_PULSO = "hola@pulso-futsal.com"
CORREO = CORREO_PULSO

LOGO = ('<svg viewBox="0 0 120 64" aria-hidden="true" focusable="false">'
        '<ellipse cx="60" cy="32" rx="55" ry="27" fill="none" stroke="#0b2545" stroke-width="5"/>'
        '<polyline points="17,32 46,32 51,27 56,36 63,15 70,46 77,32 103,32" fill="none" '
        'stroke="#e63946" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')

ICONOS = {
    "ipad": '<rect x="4" y="2" width="16" height="20" rx="2.5"/><circle cx="12" cy="18.5" r=".8"/>',
    "senal": '<path d="M2 8.5a15 15 0 0 1 20 0M5 12a10 10 0 0 1 14 0M8.5 15.5a5 5 0 0 1 7 0"/><path d="M3 3l18 18"/>',
    "enlace": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
    "banquillo": '<path d="M12 3v3M5 21l2-7h10l2 7M4 14h16"/><circle cx="12" cy="9" r="3"/>',
    "papel": '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4M10 12h5M10 16h5"/>',
    "pulso": '<path d="M2 12h5l2-4 3 9 3-12 2 7h5"/>',
    "movil": '<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
    "lupa": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
    "escudo": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
    "idiomas": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>',
    "ajustes": '<path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12M20 18h0"/><circle cx="16" cy="6" r="2"/><circle cx="10" cy="12" r="2"/><circle cx="18" cy="18" r="2"/>',
    "correo": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "tel": '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
    "wa": '<path d="M4 20l1.3-3.9A8.5 8.5 0 1 1 8 19z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1-1.5-2-1-1 1c-1-.5-2-1.5-2.5-2.5l1-1-1-2z"/>',
}


def icono(nombre):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONOS[nombre]}</svg>')


def mailto(asunto, cuerpo):
    return f"mailto:{CORREO}?subject={quote(asunto)}&body={quote(cuerpo)}"


T = {
    "es": {
        "lang": "es", "otro": "en", "ruta_otro": "en/", "pref": "",
        "title": "PULSO · Crono de partido y plataforma de rendimiento para fútbol sala",
        "desc": "PULSO: el crono de partido para el iPad y la web de rendimiento físico, partido y scouting. Usada en Inter JP Financial.",
        "saltar": "Saltar al contenido",
        "nav": [("que-es", "Qué es"), ("crono", "Crono"), ("plataforma", "Plataforma"), ("como-funciona", "Cómo funciona"), ("contacto", "Contacto")],
        "menu": "Menú",
        "etiqueta": "Fútbol sala · rendimiento y partido",
        "h1": "El partido y el físico de tu equipo, <em>en un solo sitio</em>.",
        "entradilla": "Un crono de partido para el iPad del banquillo y una web con la carga, el peso y el bienestar de cada jugador, las estadísticas de cada partido y el scouting de cada rival.",
        "cta1": "Solicita la demo", "cta2": "Cómo funciona",
        "aval_t": "En uso en Inter JP Financial",
        "aval_p": "Se usa cada semana en el club, en los entrenos y en los partidos.",
        "alt_hero_ipad": "El crono de PULSO en un iPad durante un partido: reloj, marcador y minutos de cada jugador en pista",
        "alt_hero_web": "Semáforo del equipo en la web de PULSO",
        # Qué es
        "q_h": "Qué es PULSO",
        "q_p": "Dos herramientas pensadas para el cuerpo técnico de un equipo de fútbol sala. Se contratan por separado y, juntas, se hablan: lo que apuntas en el crono pasa a la web.",
        "q_crono_t": "El crono de partido",
        "q_crono_p": "En el iPad del banquillo. Tú apuntas el partido y el informe sale solo.",
        "q_crono_l": ["Minutos y rotaciones de cada jugador", "Goles con su jugada y su quinteto", "Informe en PDF al acabar"],
        "q_web_t": "La plataforma web",
        "q_web_p": "El físico y el partido de tu equipo, en una sola web.",
        "q_web_l": ["Carga, peso y bienestar de cada jugador", "Estadísticas de cada partido y de la temporada", "Scouting de cada rival"],
        "q_ver": "Ver más",
        "q_nota": "Todas las capturas de esta página son de la demo, con jugadores, partidos y rivales inventados.",
        # Crono
        "c_et": "El crono de partido",
        "c_h": "Tú apuntas el partido. El informe sale solo.",
        "c_p": "El crono y la estadística de futsal para tu banquillo, en un iPad. Sin papeles que pasar a limpio después del partido.",
        "c_v": [("Un iPad", "Es todo lo que necesitas en el banquillo."), ("Sin cobertura", "Internet solo la primera vez. En el partido, no hace falta."), ("Sin instalar", "Ninguna tienda de apps. Se abre una dirección y ya está.")],
        "c_caps": [
            ("02_nuevo", "Preparar el partido", "Rival, convocados y los cinco que salen. La competición fija la duración y la prórroga."),
            ("03_directo", "El partido en directo", "Reloj, marcador y faltas arriba. En pista, cuánto lleva cada uno. En el banquillo, cuánto descansa."),
            ("05_jugador", "Tocas a un jugador", "Robo, corte, pérdida, disparo, falta o tarjeta. Y el cambio, en la misma ventana. Aquí, en modo Sol: claro, para pabellones con mucha luz."),
            ("04_gol", "Apuntar un gol", "Goleador, asistente y jugada. Quién estaba en pista se guarda solo: ya tienes el quinteto del gol."),
            ("06_resumen", "El resumen, en cualquier momento", "En mitad del partido o en el descanso: disparos de los dos equipos, pérdidas y recuperaciones."),
            ("09_cronograma", "Cronograma", "Quién estuvo en pista en cada minuto, con goles, faltas y disparos encima."),
            ("10_disparos_mapa", "Mapas de disparo", "Desde dónde se tira y a qué parte de la portería. Con el partido pasado en vídeo."),
            ("13_totales", "Totales de la temporada", "Todos los partidos sumados, en el propio iPad. Con copia de seguridad para pasarlo a otro."),
        ],
        "c_inf_h": "El informe del partido", "c_inf_s": "Un botón y lo tienes en PDF",
        "c_inf": [
            ("informe_p1", "Portada", "Marcador, cifras clave y estadísticas comparadas con el rival."),
            ("informe_p2", "Minutos", "Por parte y en total, jugador a jugador."),
            ("informe_p3", "Métricas de cada jugador", "Lo de cada uno en el partido, con las métricas de vídeo si se apuntó con vídeo."),
        ],
        "c_inf_nota": "Además: valoración de cada jugador, goles con su jugada y su quinteto, mapas de zona, cronograma, rotaciones y cuartetos. Se guarda en PDF desde el iPad o se envía por correo o WhatsApp. Apuntado en directo salen menos datos que pasando el partido en vídeo (sin zonas ni duelos).",
        "c_adapta_t": "Se adapta a tu equipo",
        "c_adapta_p": "La botonera del crono y las competiciones (duración de las partes, prórroga, tanda de penaltis) se configuran a lo que pida cada equipo. Funciona en castellano, inglés e italiano.",
        # Plataforma
        "p_et": "La plataforma web",
        "p_h": "El físico y el partido de tu equipo. En una sola web.",
        "p_p": "Carga, peso y bienestar de cada jugador. Estadísticas de cada partido y de la temporada. Scouting de cada rival. Desde el ordenador o el móvil.",
        "p_v": [("Carga objetiva", "La de los acelerómetros que use el club, si los usa (es opcional). Sin aparato, Borg × minutos."), ("Desde el móvil", "Los jugadores responden antes y después de entrenar. Sin instalar nada."), ("El rival, al detalle", "Cómo marca, quién tira sus penaltis y a dónde, y su portero-jugador.")],
        "p_fis_h": "Rendimiento físico", "p_fis_s": "Cada entreno, cada jugador",
        "p_fis": [
            ("01_semaforo", "El semáforo del equipo", "Una tarjeta por jugador: ACWR, carga reciente, bienestar y peso. El color dice a quién mirar primero."),
            ("02_acwr", "Carga aguda y crónica (ACWR)", "Carga de 7 días frente a la de 28, toda la temporada, con las zonas de riesgo marcadas."),
            ("03_ficha", "La ficha del jugador", "Su semáforo, su ACWR, su carga, su bienestar y su peso, con una lectura rápida."),
            ("05_carga_reciente", "¿Quién va más cargado?", "La carga reciente de cada jugador frente a la media del equipo. Y la monotonía y la fatiga de la semana."),
            ("11_well_heatmap", "Bienestar diario", "Sueño, fatiga, molestias y ánimo, sumados de 4 a 20. El rojo salta a la vista. Y el peso antes y después de cada sesión."),
            ("14_disponibilidad", "Participación y disponibilidad", "Disponible, lesión, selección, ausencia o descanso, sesión a sesión."),
        ],
        "p_par_h": "Partido, temporada y scouting", "p_par_s": "Cada partido, cada rival",
        "p_par": [
            ("20_partido", "Cada partido, de un vistazo", "Marcador, disparos, pérdidas y recuperaciones. Y el informe en PDF con un botón."),
            ("24_zonas_partido", "Zonas y portería", "Desde dónde se marca y a qué parte de la portería, a favor y en contra."),
            ("30_pases", "Mapa de pases de gol", "De dónde sale cada pase de gol y cada asistencia, y dónde acaba."),
            ("25_eficiencia", "La temporada, jugador a jugador", "Goles, asistencias y +/- en pista, normalizados a 40 minutos."),
            ("40_scout_comparativa", "Scouting de rivales", "Cómo marca cada rival, por origen del gol: banda, córner, contraataque, 5x4…"),
            ("44_pen_equipo", "Penaltis y 10 metros", "Quién tira, quién para y a qué zona. Con filtros por club y por jugador."),
        ],
        "p_inf_t": "Informes en PDF con un botón",
        "p_inf_p": "El informe del partido y, antes de cada partido, el informe del rival con dos hojas sueltas: una para nuestros porteros y otra para nuestros lanzadores. Todo lo que llega del crono se puede corregir después en la web.",
        # Por qué
        "b_h": "Por qué PULSO",
        "b_p": "Se usa cada semana en un club de élite y se ha ido puliendo con lo que pide el banquillo.",
        "b": [
            ("banquillo", "Nace en un banquillo", "La ha diseñado el preparador físico de Inter JP Financial y se usa en el club entreno a entreno y partido a partido."),
            ("papel", "Sin pasar nada a limpio", "Lo que se apunta en el partido ya es el informe. Lo que responden los jugadores ya está en la web."),
            ("pulso", "Decisiones con datos", "El semáforo dice a quién mirar primero: carga, bienestar y peso en una sola pantalla."),
            ("lupa", "El rival, antes del partido", "Cómo marca, quién tira y a dónde, y cómo se coloca su portero."),
            ("ajustes", "A la medida del club", "Botonera, competiciones, escudo, colores e idioma (castellano, inglés o italiano)."),
            ("escudo", "Tus datos, bien guardados", "Los custodiamos nosotros, conforme al RGPD. Cada equipo, con su propio acceso."),
        ],
        # Cómo funciona
        "f_h": "Cómo funciona",
        "f_p": "Tres pasos. Vosotros nos contáis cómo es vuestro club y nosotros lo dejamos listo.",
        "f": [
            ("Alta del club", "Nos dais lo básico: escudo, colores, plantilla, competiciones y quién lo va a usar. Elegís crono, web o los dos."),
            ("Nosotros lo montamos", "Configuramos vuestro crono y vuestra web, cargamos la plantilla y enseñamos a usarlo a quien lo vaya a llevar."),
            ("El club lo usa", "Desde el primer partido y el primer entreno. Cualquier duda o ajuste, nos lo decís y lo cambiamos."),
        ],
        "f_cust_t": "Los datos los custodiamos nosotros",
        "f_cust_p": "Tratamos los datos del club conforme al RGPD (Reglamento General de Protección de Datos). Cada equipo tiene su propia contraseña y solo ve lo suyo.",
        # Contacto
        "k_h": "Contacta con nosotros",
        "k_p": "Cuéntanos tu club y te enseñamos PULSO. Sin compromiso.",
        "k_demo_t": "Solicita acceso a la demo",
        "k_demo_p": "Pruébalo con datos inventados: el crono en tu iPad y la web en el ordenador o el móvil. Escríbenos y te mandamos el acceso.",
        "k_demo_b": "Pedir acceso a la demo",
        "k_demo_asunto": "PULSO: solicitud de acceso a la demo",
        "k_demo_cuerpo": "Hola, Arkaitz:\n\nMe gustaría probar la demo de PULSO.\n\nClub:\nEquipo / categoría:\nMi cargo:\nMe interesa: crono / web / los dos\n\nGracias.",
        "k_hab_t": "Hablemos",
        "k_hab_p": "Escríbenos y te respondemos lo antes posible.",
        "k_correo": "Escríbenos",
        "k_correo_asunto": "Información sobre PULSO",
        "k_correo_cuerpo": "Hola, Arkaitz:\n\nMe gustaría recibir información sobre PULSO.\n\nClub:\nEquipo / categoría:\n\nGracias.",
        "k_wa": "WhatsApp",
        "k_wa_texto": "Hola, Arkaitz. Me gustaría recibir información sobre PULSO.",
        "k_tel": "o llama al",
        "k_persona": "Arkaitz Sisniega · Preparador físico de Inter JP Financial · Experto en entrenamiento y datos de rendimiento",
        "pie": "PULSO · En uso en Inter JP Financial",
        "pie2": "Capturas de la demo, con datos inventados.",
        "marcas": "Los escudos de Inter JP Financial y de JP Financial solo indican el club en el que se usa PULSO. PULSO es un proyecto independiente de Arkaitz Sisniega: ni el club ni su patrocinador lo comercializan ni lo respaldan comercialmente.",
        "l_aviso": "Aviso legal", "l_priv": "Privacidad", "f_aviso": "aviso-legal.html", "f_priv": "privacidad.html", "volver": "Volver a la página principal",
        "ampliar": "(se abre a tamaño completo)",
        "desliza": "Desliza para ver más →",
    },
    "en": {
        "lang": "en", "otro": "es", "ruta_otro": "../", "pref": "../",
        "title": "PULSO · Match timer and performance platform for futsal",
        "desc": "PULSO: the match timer for the iPad and the web app for fitness, matches and scouting. Used at Inter JP Financial.",
        "saltar": "Skip to content",
        "nav": [("que-es", "What it is"), ("crono", "Timer"), ("plataforma", "Web app"), ("como-funciona", "How it works"), ("contacto", "Contact")],
        "menu": "Menu",
        "etiqueta": "Futsal · performance and matches",
        "h1": "Your team's matches and fitness, <em>all in one place</em>.",
        "entradilla": "A match timer for the iPad on the bench and a web app with each player's load, weight and wellness, stats for every match and scouting for every opponent.",
        "cta1": "Request the demo", "cta2": "How it works",
        "aval_t": "In use at Inter JP Financial",
        "aval_p": "Used every week at the club, in training and in matches.",
        "alt_hero_ipad": "The PULSO timer on an iPad during a match: clock, score and minutes for each player on court",
        "alt_hero_web": "Squad traffic light on the PULSO web app",
        "q_h": "What PULSO is",
        "q_p": "Two tools built for the coaching staff of a futsal team. They are sold separately and, together, they talk to each other: what you log on the timer goes to the web app.",
        "q_crono_t": "The match timer",
        "q_crono_p": "On the iPad on the bench. You log the match and the report is ready.",
        "q_crono_l": ["Minutes and rotations for each player", "Each goal with its play and the five on court", "PDF report at the final whistle"],
        "q_web_t": "The web app",
        "q_web_p": "Your team's fitness and matches, in one web app.",
        "q_web_l": ["Load, weight and wellness for every player", "Stats for every match and the whole season", "Scouting for every opponent"],
        "q_ver": "See more",
        "q_nota": "All screens on this page are from the demo, with invented players, matches and opponents.",
        "c_et": "The match timer",
        "c_h": "You log the match. The report is ready.",
        "c_p": "Futsal timer and match stats for your bench, on an iPad. No paperwork to copy out after the match.",
        "c_v": [("Just an iPad", "That is all you need on the bench."), ("No signal needed", "Internet only the first time. Not during the match."), ("Nothing to install", "No app store. Open a link and start.")],
        "c_caps": [
            ("02_nuevo", "Set up the match", "Opponent, squad and starting five. The competition sets the half length and extra time."),
            ("03_directo", "The live match", "Clock, score and fouls at the top. On court: time played by each player. On the bench: rest time."),
            ("05_jugador", "Tap a player", "Steal, interception, turnover, shot, foul or card. And the substitution, in the same window. Shown here in Sun mode: a light theme for bright venues."),
            ("04_gol", "Log a goal", "Scorer, assist and type of play. The players on court are saved automatically, so you have the five for each goal."),
            ("06_resumen", "The summary, at any moment", "During the match or at half-time: shots for both teams, turnovers and recoveries."),
            ("09_cronograma", "Match timeline", "Who was on court in each minute, with goals, fouls and shots on top."),
            ("10_disparos_mapa", "Shot maps", "Where shots come from and where they go in the goal. When you log the match from video."),
            ("13_totales", "Season totals", "Every match added up, on the iPad itself. With a backup to move it to another one."),
        ],
        "c_inf_h": "The match report", "c_inf_s": "One button and you have the PDF",
        "c_inf": [
            ("informe_p1", "Front page", "Score, key numbers and stats compared with the opponent."),
            ("informe_p2", "Minutes", "By half and in total, player by player."),
            ("informe_p3", "Each player's numbers", "What each player did in the match, plus the video metrics when logged from video."),
        ],
        "c_inf_nota": "Also: a rating for each player, goals with their play and the five on court, zone maps, timeline, rotations and groups of four. Save it as a PDF on the iPad or send it by email or WhatsApp. A match logged live has less data than one logged from video (no zones or duels). The sample report is in Spanish; the report comes in your language.",
        "c_adapta_t": "Made to suit your team",
        "c_adapta_p": "The timer's buttons and competitions (half length, extra time, penalty shoot-out) are set up to suit each team. Available in English, Spanish and Italian.",
        "p_et": "The web app",
        "p_h": "Your team's fitness and matches. In one web app.",
        "p_p": "Load, weight and wellness for every player. Stats for every match and the whole season. Scouting for every opponent. On a computer or a phone.",
        "p_v": [("Objective load", "From the accelerometers the club uses, if any (they are optional). Without a device, Borg × minutes."), ("From the phone", "Players answer before and after training. Nothing to install."), ("The opponent, in detail", "How they score, who takes their penalties and where, and their fly-goalkeeper play.")],
        "p_fis_h": "Physical performance", "p_fis_s": "Every session, every player",
        "p_fis": [
            ("01_semaforo", "The squad traffic light", "One card per player: ACWR, recent load, wellness and weight. The colour tells you who to look at first."),
            ("02_acwr", "Acute and chronic load (ACWR)", "7-day load against 28-day load, all season, with the risk zones marked."),
            ("03_ficha", "The player profile", "Traffic light, ACWR, load, wellness and weight, with a quick reading."),
            ("05_carga_reciente", "Who is carrying the most?", "Each player's recent load against the team average. Plus the week's monotony and strain."),
            ("11_well_heatmap", "Daily wellness", "Sleep, fatigue, soreness and mood, added up from 4 to 20. Red stands out. Plus weight before and after each session."),
            ("14_disponibilidad", "Participation and availability", "Available, injured, national team, absent or resting, session by session."),
        ],
        "p_par_h": "Matches, season and scouting", "p_par_s": "Every match, every opponent",
        "p_par": [
            ("20_partido", "Every match at a glance", "Score, shots, turnovers and recoveries. And the PDF report, with one button."),
            ("24_zonas_partido", "Zones and goal", "Where goals come from and which part of the goal, for and against."),
            ("30_pases", "Map of goal passes", "Where each goal pass and each assist starts, and where it ends."),
            ("25_eficiencia", "The season, player by player", "Goals, assists and on-court +/-, per 40 minutes."),
            ("40_scout_comparativa", "Opponent scouting", "How each opponent scores, by origin of the goal: side line, corner, counter-attack, 5v4…"),
            ("44_pen_equipo", "Penalties and 10 metres", "Who shoots, who saves and where. Filtered by club and by player."),
        ],
        "p_inf_t": "PDF reports with one button",
        "p_inf_p": "The match report and, before every match, the opponent report with two separate sheets: one for our goalkeepers and one for our shooters. Everything that comes from the timer can be corrected later on the web app.",
        "b_h": "Why PULSO",
        "b_p": "An elite club uses it every week, and it has been refined with what the bench asks for.",
        "b": [
            ("banquillo", "Born on the bench", "Designed by the strength and conditioning coach of Inter JP Financial and used at the club, session after session and match after match."),
            ("papel", "Nothing to copy out", "What you log during the match is already the report. What players answer is already on the web app."),
            ("pulso", "Decisions backed by data", "The traffic light shows who to look at first: load, wellness and weight on one screen."),
            ("lupa", "The opponent, before the match", "How they score, who shoots and where, and how their goalkeeper sets up."),
            ("ajustes", "Tailored to your club", "Buttons, competitions, crest, colours and language (English, Spanish or Italian)."),
            ("escudo", "Your data, kept safe", "We look after it, in line with the GDPR. Each team has its own access."),
        ],
        "f_h": "How it works",
        "f_p": "Three steps. You tell us about your club and we get everything ready.",
        "f": [
            ("Club sign-up", "Send us the basics: crest, colours, squad, competitions and who will use it. Choose the timer, the web app or both."),
            ("We set it up", "We configure your timer and your web app, load your squad and train whoever is going to use it."),
            ("Your club uses it", "From the first match and the first session. Any question or change, just tell us and we adjust it."),
        ],
        "f_cust_t": "We look after the data",
        "f_cust_p": "We handle the club's data in line with the GDPR (General Data Protection Regulation). Each team has its own password and only sees its own data.",
        "k_h": "Contact us",
        "k_p": "Tell us about your club and we will show you PULSO. No commitment.",
        "k_demo_t": "Request access to the demo",
        "k_demo_p": "Try it with invented data: the timer on your iPad and the web app on a computer or phone. Write to us and we will send you access.",
        "k_demo_b": "Request demo access",
        "k_demo_asunto": "PULSO: demo access request",
        "k_demo_cuerpo": "Hello Arkaitz,\n\nI would like to try the PULSO demo.\n\nClub:\nTeam / category:\nMy role:\nI am interested in: timer / web app / both\n\nThank you.",
        "k_hab_t": "Let's talk",
        "k_hab_p": "Write to us and we will get back to you as soon as possible.",
        "k_correo": "Email us",
        "k_correo_asunto": "Information about PULSO",
        "k_correo_cuerpo": "Hello Arkaitz,\n\nI would like some information about PULSO.\n\nClub:\nTeam / category:\n\nThank you.",
        "k_wa": "WhatsApp",
        "k_wa_texto": "Hello Arkaitz, I would like some information about PULSO.",
        "k_tel": "or call",
        "k_persona": "Arkaitz Sisniega · Strength and conditioning coach at Inter JP Financial · Expert in training and performance data",
        "pie": "PULSO · In use at Inter JP Financial",
        "pie2": "Demo screens, with invented data.",
        "marcas": "The Inter JP Financial and JP Financial crests only show the club where PULSO is used. PULSO is an independent project by Arkaitz Sisniega: neither the club nor its sponsor sells or commercially endorses it.",
        "l_aviso": "Legal notice", "l_priv": "Privacy", "f_aviso": "legal-notice.html", "f_priv": "privacy.html", "volver": "Back to the home page",
        "ampliar": "(opens full size)",
        "desliza": "Swipe to see more →",
    },
}


def tam(ruta):
    with Image.open(RAIZ / ruta) as im:
        return im.size


def img(ruta, alt, pref, clase="", lazy=True, sizes=None):
    w, h = tam(ruta)
    extra = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return f'<img src="{pref}{ruta}" width="{w}" height="{h}" alt="{escape(alt)}"{extra}{f" class={chr(34)}{clase}{chr(34)}" if clase else ""}>'


def figura(ruta, titulo, texto, t, clase=""):
    return (f'<figure class="{clase}"><a href="{t["pref"]}{ruta}" target="_blank" rel="noopener" '
            f'aria-label="{escape(titulo)} {t["ampliar"]}">{img(ruta, titulo + ". " + texto, t["pref"])}</a>'
            f'<figcaption><strong>{escape(titulo)}</strong><span>{escape(texto)}</span></figcaption></figure>')


def pagina(t):
    L, p = t["lang"], t["pref"]
    nav = "".join(f'<a href="#{a}">{escape(n)}</a>' for a, n in t["nav"])
    es_actual = L == "es"
    idioma = ('<div class="idioma" role="group" aria-label="Idioma / Language">'
              + (f'<span aria-current="true" lang="es">ES</span><a href="en/index.html" lang="en" hreflang="en">EN</a>' if es_actual
                 else f'<a href="../index.html" lang="es" hreflang="es">ES</a><span aria-current="true" lang="en">EN</span>')
              + '</div>')
    m_demo = mailto(t["k_demo_asunto"], t["k_demo_cuerpo"])
    m_info = mailto(t["k_correo_asunto"], t["k_correo_cuerpo"])
    ventajas = lambda lista: "".join(f'<div class="ventaja"><strong>{escape(a)}</strong><span>{escape(b)}</span></div>' for a, b in lista)
    lista = lambda xs: "".join(f"<li>{escape(x)}</li>" for x in xs)
    caps_crono = "".join(figura(f"img/{L}/crono_{n}.webp", a, b, t, "oscura") for n, a, b in t["c_caps"])
    caps_inf = "".join(figura(f"img/{n}.webp", a, b, t, "doc") for n, a, b in t["c_inf"])
    caps_fis = "".join(figura(f"img/{L}/web_{n}.webp", a, b, t, "ancha" if n == "03_ficha" else "") for n, a, b in t["p_fis"])
    caps_par = "".join(figura(f"img/{L}/web_{n}.webp", a, b, t) for n, a, b in t["p_par"])
    beneficios = "".join(f'<div class="tarjeta"><div class="icono">{icono(i)}</div><h3>{escape(a)}</h3><p>{escape(b)}</p></div>' for i, a, b in t["b"])
    pasos = "".join(f"<li><h3>{escape(a)}</h3><p>{escape(b)}</p></li>" for a, b in t["f"])
    url = DOMINIO + ("/" if es_actual else "/en/")

    return f"""<!doctype html>
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(t["title"])}</title>
<meta name="description" content="{escape(t["desc"])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="es" href="{DOMINIO}/">
<link rel="alternate" hreflang="en" href="{DOMINIO}/en/">
<link rel="alternate" hreflang="x-default" href="{DOMINIO}/">
<meta name="theme-color" content="#0b2545">
<meta property="og:type" content="website">
<meta property="og:title" content="{escape(t["title"])}">
<meta property="og:description" content="{escape(t["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMINIO}/img/{L}/crono_03_directo.webp">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
<link rel="stylesheet" href="{p}styles.css">
</head>
<body>
<a class="salto" href="#contenido">{t["saltar"]}</a>
<header class="cabecera">
  <div class="envoltura">
    <a class="marca" href="#inicio" aria-label="PULSO">{LOGO}<span>PULSO</span></a>
    <nav class="nav" aria-label="{t["menu"]}">{nav}</nav>
    <div class="acciones-cab">
      {idioma}
      <details class="menu"><summary>{t["menu"]}</summary><nav aria-label="{t["menu"]}">{nav}</nav></details>
    </div>
  </div>
</header>

<main id="contenido">
<section class="portada" id="inicio">
  <div class="envoltura">
    <div>
      <span class="etiqueta">{t["etiqueta"]}</span>
      <h1>{t["h1"]}</h1>
      <p class="entradilla">{escape(t["entradilla"])}</p>
      <div class="botones">
        <a class="boton boton-1" href="#contacto">{t["cta1"]}</a>
        <a class="boton boton-2" href="#como-funciona">{t["cta2"]}</a>
      </div>
      <div class="aval">
        <p><strong>{t["aval_t"]}</strong>{t["aval_p"]}</p>
        <div class="aval-logos">{img("img/inter.webp", "Escudo de Inter fútbol sala", p, "inter")}{img("img/jp_financial.webp", "Logo de JP Financial", p, "jp")}</div>
      </div>
    </div>
    <div class="escena">
      <div class="marco-ipad">{img(f"img/{L}/crono_03_directo.webp", t["alt_hero_ipad"], p, lazy=False)}</div>
      <div class="marco-web"><div class="barra"><i></i><i></i><i></i></div>{img(f"img/{L}/web_01_semaforo.webp", t["alt_hero_web"], p, lazy=False)}</div>
    </div>
  </div>
</section>

<section class="seccion" id="que-es">
  <div class="envoltura">
    <div class="cabeza"><h2>{t["q_h"]}</h2><p>{escape(t["q_p"])}</p></div>
    <div class="rejilla dos">
      <div class="tarjeta producto"><div class="icono">{icono("ipad")}</div><h3>{t["q_crono_t"]}</h3><p>{escape(t["q_crono_p"])}</p><ul>{lista(t["q_crono_l"])}</ul><a class="boton boton-2" href="#crono">{t["q_ver"]}</a></div>
      <div class="tarjeta producto"><div class="icono">{icono("pulso")}</div><h3>{t["q_web_t"]}</h3><p>{escape(t["q_web_p"])}</p><ul>{lista(t["q_web_l"])}</ul><a class="boton boton-2" href="#plataforma">{t["q_ver"]}</a></div>
    </div>
    <p class="nota">{t["q_nota"]}</p>
  </div>
</section>

<section class="seccion alterna" id="crono">
  <div class="envoltura">
    <div class="cabeza"><span class="etiqueta">{t["c_et"]}</span><h2>{t["c_h"]}</h2><p>{escape(t["c_p"])}</p></div>
    <div class="ventajas">{ventajas(t["c_v"])}</div>
    <p class="desliza" aria-hidden="true">{t["desliza"]}</p><div class="capturas">{caps_crono}</div>
    <div class="subtitulo"><h3>{t["c_inf_h"]}</h3><span>{t["c_inf_s"]}</span></div>
    <p class="desliza" aria-hidden="true">{t["desliza"]}</p><div class="capturas tres">{caps_inf}</div>
    <p class="nota">{escape(t["c_inf_nota"])}</p>
    <div class="aviso-adapta"><div class="icono">{icono("ajustes")}</div><div><h3>{t["c_adapta_t"]}</h3><p>{escape(t["c_adapta_p"])}</p></div></div>
  </div>
</section>

<section class="seccion" id="plataforma">
  <div class="envoltura">
    <div class="cabeza"><span class="etiqueta">{t["p_et"]}</span><h2>{t["p_h"]}</h2><p>{escape(t["p_p"])}</p></div>
    <div class="ventajas">{ventajas(t["p_v"])}</div>
    <div class="subtitulo"><h3>{t["p_fis_h"]}</h3><span>{t["p_fis_s"]}</span></div>
    <p class="desliza" aria-hidden="true">{t["desliza"]}</p><div class="capturas">{caps_fis}</div>
    <div class="subtitulo"><h3>{t["p_par_h"]}</h3><span>{t["p_par_s"]}</span></div>
    <p class="desliza" aria-hidden="true">{t["desliza"]}</p><div class="capturas">{caps_par}</div>
    <div class="aviso-adapta"><div class="icono">{icono("papel")}</div><div><h3>{t["p_inf_t"]}</h3><p>{escape(t["p_inf_p"])}</p></div></div>
  </div>
</section>

<section class="seccion alterna" id="por-que">
  <div class="envoltura">
    <div class="cabeza"><h2>{t["b_h"]}</h2><p>{escape(t["b_p"])}</p></div>
    <div class="rejilla tres">{beneficios}</div>
  </div>
</section>

<section class="seccion" id="como-funciona">
  <div class="envoltura">
    <div class="cabeza"><h2>{t["f_h"]}</h2><p>{escape(t["f_p"])}</p></div>
    <ol class="pasos">{pasos}</ol>
    <div class="custodia"><div class="icono">{icono("escudo")}</div><div><h3>{t["f_cust_t"]}</h3><p>{escape(t["f_cust_p"])}</p></div></div>
  </div>
</section>

<section class="seccion contacto" id="contacto">
  <div class="envoltura">
    <div class="cabeza"><h2>{t["k_h"]}</h2><p>{escape(t["k_p"])}</p></div>
    <div class="rejilla dos">
      <div class="caja">
        <h3>{t["k_demo_t"]}</h3>
        <p>{escape(t["k_demo_p"])}</p>
        <div class="botones"><a class="boton boton-claro" href="{escape(m_demo)}">{icono("correo")}{t["k_demo_b"]}</a></div>
      </div>
      <div class="caja">
        <h3>{t["k_hab_t"]}</h3>
        <p>{escape(t["k_hab_p"])}</p>
        <div class="botones">
          <a class="boton boton-claro" href="{escape(m_info)}">{icono("correo")}{t["k_correo"]}</a>
        </div>
        <p class="persona">{escape(t["k_persona"])}<br><a href="mailto:{CORREO}" style="color:#fff">{CORREO}</a></p>
      </div>
    </div>
  </div>
</section>
</main>

<footer class="pie">
  <div class="envoltura">
    <span>{t["pie"]}</span>
    <span>{t["pie2"]}</span>
    {idioma}
    <p class="marcas">{escape(t["marcas"])}</p>
  </div>
</footer>
<script>document.querySelectorAll(".menu nav a").forEach(function(a){{a.addEventListener("click",function(){{a.closest("details").removeAttribute("open");}});}});</script>
</body>
</html>
"""


PROV_ES = "Zoho Mail (Zoho Corporation, servidores en la UE)"
PROV_EN = "Zoho Mail (Zoho Corporation, EU servers)"
PEND = '<mark class="pendiente">[PENDIENTE: {}]</mark>'

LEGAL = {
    "es": {
        "aviso": ("Aviso legal", "aviso-legal.html", "en/legal-notice.html", [
            ("Titular de esta web", f"""<ul>
<li><strong>Titular:</strong> {PEND.format("razón social de la SL")}</li>
<li><strong>CIF:</strong> {PEND.format("CIF de la SL")}</li>
<li><strong>Domicilio social:</strong> {PEND.format("domicilio")}</li>
<li><strong>Datos registrales:</strong> {PEND.format("Registro Mercantil de …, tomo, folio, hoja e inscripción")}</li>
<li><strong>Correo:</strong> <a href="mailto:{CORREO}">{CORREO}</a></li>
<li><strong>Dominio:</strong> pulso-futsal.com</li>
</ul><p>Estos datos se dan en cumplimiento de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico (LSSI).</p>"""),
            ("Qué es esta web", "<p>Es una web informativa sobre PULSO, un crono de partido y una plataforma web de rendimiento para equipos de fútbol sala. No se vende nada en ella ni se recoge ningún dato a través de formularios: el contacto se hace por correo, WhatsApp o teléfono.</p>"),
            ("Marcas y escudos", "<p>Los escudos y nombres de Inter JP Financial y de JP Financial pertenecen a sus titulares y aparecen solo para indicar el club en el que se usa PULSO. PULSO es un proyecto independiente de Arkaitz Sisniega Gómez: ni el club ni su patrocinador lo comercializan ni lo respaldan comercialmente.</p>"),
            ("Contenidos", "<p>Los textos, el diseño y las capturas de esta web son de su titular. Todas las capturas son de una demostración con jugadores, partidos y rivales inventados. No se permite copiarlos para un uso comercial sin permiso.</p>"),
            ("Responsabilidad", "<p>La información de esta web es orientativa y describe el producto; las condiciones concretas de cada club se acuerdan por separado. Los enlaces a servicios externos (WhatsApp, el correo electrónico) llevan a servicios de terceros, con sus propias condiciones.</p>"),
            ("Privacidad y cookies", '<p>Cómo se tratan los datos de quien nos escribe está en la <a href="privacidad.html">política de privacidad</a>. Esta web no usa cookies.</p>'),
        ]),
        "priv": ("Política de privacidad", "privacidad.html", "en/privacy.html", [
            ("Responsable", f"""<ul>
<li><strong>Responsable del tratamiento:</strong> {PEND.format("razón social de la SL")}</li>
<li><strong>CIF:</strong> {PEND.format("CIF de la SL")}</li>
<li><strong>Domicilio social:</strong> {PEND.format("domicilio")}</li>
<li><strong>Datos registrales:</strong> {PEND.format("Registro Mercantil de …, tomo, folio, hoja e inscripción")}</li>
<li><strong>Contacto:</strong> <a href="mailto:{CORREO}">{CORREO}</a></li>
</ul>"""),
            ("Qué datos recibimos", "<p>Esta web no tiene formularios ni recoge datos por sí misma. Solo recibimos los datos que tú nos mandas al escribirnos por correo o por WhatsApp, o al llamarnos: normalmente tu nombre, tu correo o teléfono, tu club y tu cargo, y lo que nos cuentes en el mensaje.</p>"),
            ("Para qué los usamos", "<p>Para contestar a tu consulta o a tu solicitud de acceso a la demo y, si te interesa, preparar una propuesta para tu club. No los usamos para nada más, no te mandamos publicidad sin pedírtelo y no tomamos decisiones automatizadas con ellos.</p>"),
            ("Base legal", "<p>Tu consentimiento al escribirnos (artículo 6.1.a del Reglamento General de Protección de Datos, RGPD) y, si nos pides una propuesta o la demo, la aplicación de medidas precontractuales a petición tuya (artículo 6.1.b del RGPD).</p>"),
            ("Cuánto tiempo los guardamos", f"<p>El tiempo necesario para atender tu solicitud. Si después no hay relación con tu club, los borramos como máximo 12 meses después del último contacto. Si se firma un acuerdo, se guardan mientras dure y durante los plazos que exija la ley.</p>"),
            ("A quién se los damos", f"<p>A nadie, salvo obligación legal. Los mensajes viajan y se guardan en los servicios que tú elijas para escribirnos: el correo ({PROV_ES}) o WhatsApp (de Meta). Estos proveedores pueden tratar datos fuera del Espacio Económico Europeo, con las garantías que recogen sus propias políticas.</p>"),
            ("Tus derechos", f"""<p>Puedes pedir en cualquier momento <strong>acceder</strong> a tus datos, <strong>rectificarlos</strong>, <strong>suprimirlos</strong>, <strong>oponerte</strong> a su tratamiento, <strong>limitarlo</strong> o llevártelos (<strong>portabilidad</strong>), y retirar tu consentimiento. Basta con escribir a <a href="mailto:{CORREO}">{CORREO}</a> diciendo qué derecho quieres ejercer. Si crees que no hemos tratado bien tus datos, puedes reclamar ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es" rel="noopener">www.aepd.es</a>).</p>"""),
            ("Cookies y analítica", "<p>Esta web <strong>no usa cookies</strong>, ni propias ni de terceros, y <strong>no tiene analítica</strong> ni herramientas de seguimiento. No carga fuentes, librerías ni contenidos de otros sitios.</p><p>La web está alojada en GitHub Pages (GitHub, Inc.). Como cualquier servidor, GitHub puede registrar datos técnicos de la conexión, como la dirección IP, por motivos de seguridad, según su propia política de privacidad.</p>"),
        ]),
        "actualizado": "Última actualización: 16 de noviembre de 2026.",
    },
    "en": {
        "aviso": ("Legal notice", "en/legal-notice.html", "aviso-legal.html", [
            ("Owner of this website", f"""<ul>
<li><strong>Owner:</strong> {PEND.format("company name of the SL")}</li>
<li><strong>Tax ID (CIF):</strong> {PEND.format("company tax ID")}</li>
<li><strong>Registered office:</strong> {PEND.format("address")}</li>
<li><strong>Registry details:</strong> {PEND.format("Commercial Registry of …, volume, folio, sheet and entry")}</li>
<li><strong>Email:</strong> <a href="mailto:{CORREO}">{CORREO}</a></li>
<li><strong>Domain:</strong> pulso-futsal.com</li>
</ul><p>This information is given under Spanish Law 34/2002 on information society services and e-commerce (LSSI).</p>"""),
            ("What this website is", "<p>It is an information website about PULSO, a match timer and a performance web app for futsal teams. Nothing is sold on it and no data is collected through forms: contact is by email, WhatsApp or phone.</p>"),
            ("Trademarks and crests", "<p>The crests and names of Inter JP Financial and JP Financial belong to their owners and appear only to show the club where PULSO is used. PULSO is an independent project by Arkaitz Sisniega Gómez: neither the club nor its sponsor sells or commercially endorses it.</p>"),
            ("Content", "<p>The texts, design and screenshots on this website belong to its owner. All screenshots come from a demo with invented players, matches and opponents. They may not be copied for commercial use without permission.</p>"),
            ("Liability", "<p>The information on this website describes the product and is for guidance only; the terms for each club are agreed separately. Links to external services (WhatsApp, email) lead to third-party services with their own terms.</p>"),
            ("Privacy and cookies", '<p>How we handle the data of people who write to us is explained in the <a href="privacy.html">privacy policy</a>. This website does not use cookies.</p>'),
        ]),
        "priv": ("Privacy policy", "en/privacy.html", "privacidad.html", [
            ("Data controller", f"""<ul>
<li><strong>Controller:</strong> {PEND.format("company name of the SL")}</li>
<li><strong>Tax ID (CIF):</strong> {PEND.format("company tax ID")}</li>
<li><strong>Registered office:</strong> {PEND.format("address")}</li>
<li><strong>Registry details:</strong> {PEND.format("Commercial Registry of …, volume, folio, sheet and entry")}</li>
<li><strong>Contact:</strong> <a href="mailto:{CORREO}">{CORREO}</a></li>
</ul>"""),
            ("What data we receive", "<p>This website has no forms and collects no data by itself. We only receive the data you send us when you write to us by email or WhatsApp, or call us: usually your name, your email or phone number, your club and role, and whatever you tell us in your message.</p>"),
            ("What we use it for", "<p>To answer your question or your demo access request and, if you are interested, to prepare a proposal for your club. We do not use it for anything else, we do not send you advertising you have not asked for and we make no automated decisions with it.</p>"),
            ("Legal basis", "<p>Your consent when you write to us (Article 6.1.a of the General Data Protection Regulation, GDPR) and, if you ask us for a proposal or the demo, steps taken at your request before a contract (Article 6.1.b GDPR).</p>"),
            ("How long we keep it", f"<p>As long as needed to deal with your request. If no relationship with your club follows, we delete it at the latest 12 months after the last contact. If an agreement is signed, it is kept while the agreement lasts and for the periods required by law.</p>"),
            ("Who we share it with", f"<p>Nobody, unless the law requires it. Messages travel through and are stored in the services you choose to write to us: email ({PROV_EN}) or WhatsApp (by Meta). These providers may process data outside the European Economic Area, with the safeguards set out in their own policies.</p>"),
            ("Your rights", f"""<p>You may at any time ask to <strong>access</strong>, <strong>rectify</strong> or <strong>erase</strong> your data, <strong>object</strong> to or <strong>restrict</strong> its processing, or take it with you (<strong>portability</strong>), and withdraw your consent. Just write to <a href="mailto:{CORREO}">{CORREO}</a> saying which right you want to exercise. If you think we have not handled your data properly, you can complain to the Spanish Data Protection Agency (<a href="https://www.aepd.es" rel="noopener">www.aepd.es</a>) or the authority in your country.</p>"""),
            ("Cookies and analytics", "<p>This website <strong>does not use cookies</strong>, first-party or third-party, and has <strong>no analytics</strong> or tracking tools. It does not load fonts, libraries or content from other sites.</p><p>The website is hosted on GitHub Pages (GitHub, Inc.). Like any server, GitHub may log technical connection data, such as the IP address, for security purposes, under its own privacy policy.</p>"),
        ]),
        "actualizado": "Last updated: 16 November 2026.",
    },
}


def pagina_legal(t, clave):
    L = t["lang"]
    titulo, ruta, ruta_otro, bloques = LEGAL[L][clave]
    p = t["pref"]
    inicio = "./" if L == "es" else "./"
    otro = Path(ruta_otro).name
    otro_href = ("en/" + otro) if L == "es" else ("../" + otro)
    idioma = ('<div class="idioma" role="group" aria-label="Idioma / Language">'
              + (f'<span aria-current="true" lang="es">ES</span><a href="{otro_href}" lang="en" hreflang="en">EN</a>' if L == "es"
                 else f'<a href="{otro_href}" lang="es" hreflang="es">ES</a><span aria-current="true" lang="en">EN</span>')
              + '</div>')
    cuerpo = "".join(f"<h2>{escape(h)}</h2>{c}" for h, c in bloques)
    return f"""<!doctype html>
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(titulo)} · PULSO</title>
<meta name="robots" content="noindex">
<meta name="theme-color" content="#0b2545">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
<link rel="stylesheet" href="{p}styles.css">
</head>
<body>
<header class="cabecera">
  <div class="envoltura">
    <a class="marca" href="index.html" aria-label="PULSO">{LOGO}<span>PULSO</span></a>
    <div class="acciones-cab" style="margin-left:auto">{idioma}</div>
  </div>
</header>
<main class="legal envoltura">
  <p><a href="index.html">← {t["volver"]}</a></p>
  <h1>{escape(titulo)}</h1>
  {cuerpo}
  <p class="nota">{LEGAL[L]["actualizado"]}</p>
</main>
<footer class="pie">
  <div class="envoltura">
    <span>{t["pie"]}</span>
    <span class="legales"><a href="{t["f_aviso"]}">{t["l_aviso"]}</a> · <a href="{t["f_priv"]}">{t["l_priv"]}</a></span>
  </div>
</footer>
</body>
</html>
"""


FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0b2545"/>'
           '<polyline points="8,34 22,34 26,28 30,40 35,16 40,48 44,34 56,34" fill="none" stroke="#e63946" '
           'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>\n')

if __name__ == "__main__":
    (RAIZ / "index.html").write_text(pagina(T["es"]), encoding="utf-8")
    (RAIZ / "en").mkdir(exist_ok=True)
    (RAIZ / "en" / "index.html").write_text(pagina(T["en"]), encoding="utf-8")
    (RAIZ / "favicon.svg").write_text(FAVICON, encoding="utf-8")
    for L in ("es", "en"):
        # 16/11/2026: sin páginas legales, como arsis.run (decisión de Arkaitz).
        # Se reactivan cuando exista la SL: descomentar y rellenar LEGAL.
        # for clave in ("aviso", "priv"):
        #     (RAIZ / LEGAL[L][clave][1]).write_text(pagina_legal(T[L], clave), encoding="utf-8")
        pass
    print("OK: index.html y en/index.html")
