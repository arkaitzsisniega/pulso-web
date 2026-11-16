# PULSO — web informativa

Web estática de PULSO (castellano en `index.html`, inglés en `en/index.html`).
Sin servicios de terceros, sin formularios y sin fuentes ni librerías externas.

## Cambiar textos o imágenes

Los textos de los dos idiomas están juntos en `build.py` (diccionario `T`).
Después de tocarlos:

```bash
/usr/bin/python3 build.py
```

Las capturas están en `img/es/` e `img/en/` (WebP, todas de la demo con datos inventados).
Estilos en `styles.css`. `previews/` son capturas de la página completa para revisarla; no hace falta publicarlas.

## Verla en local

```bash
cd ~/Desktop/Claude/pulso-web && python3 -m http.server 8765
# y abrir http://127.0.0.1:8765
```

## Publicarla en GitHub Pages (cuando esté comprado pulso-futsal.com)

1. Crear un repositorio en GitHub (p. ej. `pulso-web`) y subir esta carpeta:
   `git remote add origin git@github.com:arkaitzsisniega/pulso-web.git && git push -u origin main`
2. En GitHub: **Settings → Pages → Source: Deploy from a branch → `main` / raíz**.
3. El archivo `CNAME` ya dice `pulso-futsal.com`. En el proveedor del dominio, crear:
   - 4 registros **A** para `pulso-futsal.com` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - 1 registro **CNAME** para `www` → `arkaitzsisniega.github.io`
4. Cuando GitHub verifique el dominio, marcar **Enforce HTTPS**.

## Páginas legales

`aviso-legal.html` / `privacidad.html` (y `en/legal-notice.html` / `en/privacy.html`) se generan también con `build.py`.
Los huecos marcados `[PENDIENTE]` (razón social, CIF, domicilio social y datos del Registro Mercantil de la SL) hay que rellenarlos antes de publicar.

Correo de contacto: `CORREO_PULSO` en `build.py` (hola@pulso-futsal.com, Zoho).
La web no usa cookies ni analítica: si algún día se añade algo así, hay que cambiar la política de privacidad.
