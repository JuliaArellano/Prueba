import streamlit as st
import comtypes.client
import os

# Ruta local del archivo .ipt
ruta_archivo = "Stent_v2.ipt"  # Cambia esto si es necesario

st.title("Visor automático de archivos .ipt de Autodesk Inventor")

# Verificar si el archivo existe en el servidor
if os.path.exists(ruta_archivo):
    st.success("¡Archivo .ipt encontrado y cargado automáticamente!")

    try:
        # Iniciar Autodesk Inventor
        inventor = comtypes.client.CreateObject("Inventor.Application")
        inventor.Visible = True

        # Abrir el archivo .ipt
        documento = inventor.Documents.Open(os.path.abspath(ruta_archivo))
        st.write("Nombre del archivo:", documento.DisplayName)

        # Mostrar el tipo de documento y algunas propiedades iniciales
        st.write(f"Tipo de documento: {documento.DocumentType}")
        st.write(f"¿El documento está guardado?: {'Sí' if documento.Saved else 'No'}")

        # Obtener la definición del componente (pieza)
        pieza = documento.ComponentDefinition
        st.write(f"Componente: {pieza.Name}")

        # 🔄 Mostrar información de los bocetos
        bocetos = pieza.Sketches
        st.write(f"Cantidad de bocetos: {bocetos.Count}")
        for i in range(1, bocetos.Count + 1):
            boceto = bocetos.Item(i)
            st.write(f"Boceto {i}: {boceto.Name}")

        # 🔄 Mostrar información de las bobinas
        bobinas = pieza.Features.RevolveFeatures
        st.write(f"Cantidad de bobinas: {bobinas.Count}")
        for i in range(1, bobinas.Count + 1):
            bobina = bobinas.Item(i)
            st.write(f"Bobina {i}: {bobina.Name}, Volumen: {bobina.MassProperties.Volume:.2f} cm³")

        # Ejemplo: mostrar el volumen total de la pieza
        volumen_total = pieza.MassProperties.Volume
        masa_total = pieza.MassProperties.Mass

        # Mostrar propiedades generales de la pieza
        st.write(f"Volumen total de la pieza: {volumen_total:.2f} cm³")
        st.write(f"Masa total de la pieza: {masa_total:.2f} g")

        # Botón para procesar
        if st.button("Procesar archivo"):
            # Aquí agregarías el código para hacer más análisis o procesamientos específicos
            st.write("¡Procesando archivo y realizando cálculos adicionales...!")
            # Aquí podrías continuar con el procesamiento de la pieza o mostrar más detalles

        # Cerrar el documento después de mostrar la información
        documento.Close()

    except Exception as e:
        st.error(f"Error al procesar el archivo con Inventor: {e}")

else:
    st.error("No se encontró el archivo .ipt en el servidor.")
