# 📘 Clase 6: Pruebas completas de API con conexión real

## 🎯 Objetivo

Validar el funcionamiento completo de una API conectando frontend, backend y lógica de datos, mediante pruebas manuales y automáticas.

---

## 🧠 ¿Qué aprenderás?

* Validar endpoints de una API
* Detectar errores comunes (duplicados, datos inválidos, IDs inexistentes)
* Probar servicios con Postman
* Automatizar pruebas con pytest
* Aplicar buenas prácticas en manejo de errores

---

## 🏗️ Estructura del proyecto

```
mi_api/
│
├── app/
│   └── main.py
│
├── tests/
│   └── test_users.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalación

1. Crear entorno virtual:

```
python -m venv venv
```

2. Activar entorno:

* Windows:

```
venv\Scripts\activate
```

* Mac/Linux:

```
source venv/bin/activate
```

3. Instalar dependencias:

```
pip install -r requirements.txt
```

---

## 📦 requirements.txt

```
fastapi
uvicorn
pytest
httpx
pydantic[email]
```

---

## 🚀 Ejecutar la API

```
uvicorn app.main:app --reload
```

📍 URL base:

```
http://127.0.0.1:8000
```

---

## 📬 Endpoints

### 🔹 Crear usuario

**POST** `/users`

```
{
  "id": 1,
  "name": "Maria",
  "email": "maria@email.com"
}
```

---

### 🔹 Crear múltiples usuarios

**POST** `/users/bulk`

```
[
  {
    "id": 2,
    "name": "Juan",
    "email": "juan@email.com"
  },
  {
    "id": 3,
    "name": "Ana",
    "email": "ana@email.com"
  }
]
```

---

### 🔹 Obtener todos los usuarios

**GET** `/users`

---

### 🔹 Obtener usuario por ID

**GET** `/users/{id}`

---

### 🔹 Actualizar usuario

**PUT** `/users/{id}`

```
{
  "id": 1,
  "name": "Maria Updated",
  "email": "maria_new@email.com"
}
```

---

### 🔹 Eliminar usuario

**DELETE** `/users/{id}`

---

## 🧪 Pruebas manuales (Postman)

Puedes probar:

* Crear usuario
* Consultar usuarios
* Actualizar datos
* Eliminar registros
* Probar errores

---

## 🤖 Pruebas automáticas

Ejecutar:

```
pytest
```

✔ Resultado esperado:

```
Todos los tests deben pasar correctamente
```

---

## ⚠️ Casos de prueba importantes

* Email duplicado → 409 Conflict
* Usuario no encontrado → 404 Not Found
* Datos inválidos → 422 Unprocessable Entity
* Actualización o eliminación de usuario inexistente

---

## 🧠 Conceptos clave

* Uso correcto de códigos HTTP
* Validación con Pydantic
* Testing manual vs automático
* Flujo CRUD completo

---

## 🎯 Actividad en clase

1. Probar endpoints en Postman
2. Ejecutar pruebas con pytest
3. Identificar errores
4. Corregir la API

---

## 💬 Frase clave

> Una API no solo debe funcionar, también debe manejar correctamente los errores.

---

## 🚀 Bonus

* Agregar nuevos campos al modelo
* Implementar validaciones adicionales
* Mejorar cobertura de pruebas
