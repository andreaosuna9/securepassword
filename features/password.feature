Feature: Verificación de contraseñas seguras

Scenario: Contraseña válida
Given que el usuario escribe una contraseña
When ingresa "Password123@"
Then el botón continuar debe habilitarse

Scenario: Contraseña inválida
Given que el usuario escribe "12345"
When el sistema evalúa la contraseña
Then el botón continuar debe permanecer deshabilitado

Scenario: Generar contraseña con una palabra
Given que el usuario escribe "perrito"
When presiona generar
Then el sistema debe sugerir contraseñas seguras

Scenario: Generar contraseña con cuatro palabras
Given que el usuario escribe "playa tacos perro mazatlan"
When presiona generar
Then el sistema debe mostrar sugerencias seguras

Scenario: Página de felicitación
Given que la contraseña cumple todos los requisitos
When el usuario presiona continuar
Then el sistema debe mostrar la página de felicitación