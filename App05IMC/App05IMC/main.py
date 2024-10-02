import flet as ft

def calcular_imc(txtPeso,txtAltura,lblIMC,page):
    try:
        peso=float(txtPeso.value)
        altura=float(txtAltura.value)
        imc=peso/(altura**2)
        lblIMC.value=f"Tu IMC es: {imc:.2f}"
        page.update()
        
    #funcion para cerrar el cuadro de dialogo 
        def cerrar_dialogo():
            page.dialog.open=True
    
    #validar condiciones del IMC
        if imc<18.5:
        dialog = ft.AlertDialog(         
                title=ft.Text("Resultado de IMC"),
                content=ft.Text("Actualmente estas bajo peso"),
                actions=[
                    ft.TextButton("OK", on_click=cerrar_dialogo)
                ]
        )        
        elif imc >= 18.5 and imc < 24.9:
        dialog = ft.AlertDialog(         
                title=ft.Text("Resultado de IMC"),
                content=ft.Text("Tu peso es normal"),
                actions=[
                    ft.TextButton("OK", on_click=cerrar_dialogo)
                ]
        )
        elif imc >= 25 and imc < 30:
        dialog = ft.AlertDialog(         
                title=ft.Text("Resultado de IMC"),
                content=ft.Text("Tienes sobrepeso"),
                actions=[
                    ft.TextButton("OK", on_click=cerrar_dialogo)
                ]
            )
        else:
            
                dialog = ft.AlertDialog(         
                    title=ft.Text("Resultado de IMC"),
                    content=ft.Text("Tienes obesidad"),
                    actions=[ft.TextButton("OK", on_click=cerrar_dialogo)],
                )
        
    except ValueError:
        
    def cerrar_dialogo(e):
        page.dialog.open=False
        page.update()
        
        dialog=ft.AlertDialog(   
            title=ft.Text("Error"),
            content=ft.Text("Debes ingresar valores numericos"),
            actions=[ft.TextButton("OK", on_click=cerrar_dialogo)],
        )

def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.bgcolor="pink"
    
    txtPeso=ft.TextField(label="Ingresa tu peso")
    txtAltura=ft.TextField(label="Ingresa tu Altura")
    lblIMC=ft.Text("Tu IMC es:")
    
    img=ft.Image(src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
                width=200,
                height=200
    
                )
    btnCalcular=ft.ElevatedButton(text="Calcular", on_click=on_calcular_clik)
    btnLimpiar=ft.ElevatedButton(text="Limpiar", on_click=Limpiar)
    
    
    page.add( 
        ft.Column(        
            controls=[txtPeso,
                    txtAltura,
                    lblIMC
                    ],alignment="CENTER"),
            
        ft.Row(
            controls=[
                img
            ],alignment="CENTER"),
        ft.Row( 
            controls=[
                    btnCalcular,
                    btnLimpiar
                    ],alignment="CENTER")
    )
            
            
            
ft.app(target=main)
