import scrapy

########################################################################################################################
#    La estructura de esta clase se compondrá de:
#       1. Importación de librerías: En primer lugar, se deben importar las librerías necesarias para el proyecto. 
#          Algunas librerías comunes para realizar scraping son: requests para realizar solicitudes HTTP, beautifulsoup4 
#          para analizar y extraer información de páginas web, scrapy para construir spiders web y realizar scraping de 
#          manera más avanzada, entre otras.
#
#      2. Definición de variables de entrada: Para la URL de búsqueda con filtros parametrizados, se deben definir las 
#         variables de entrada necesarias. Estas variables pueden ser pasadas como argumentos al script o leídas desde 
#         un archivo de configuración.
#  
#      3. Construcción de la URL: Con las variables de entrada, se debe construir la URL completa que se utilizará para 
#         obtener la información de la página web. Esto puede incluir la definición de los parámetros de filtro, que se 
#         deben agregar a la URL como cadenas de consulta.
#
#      4. Realización de solicitudes HTTP: Usando la librería requests, se debe realizar una solicitud HTTP a la URL 
#         construida en el paso anterior. Esto retornará el contenido HTML de la página web solicitada.
#
#      5. Análisis y extracción de información: Con la librería beautifulsoup4, se debe analizar el contenido HTML de la 
#         página web y extraer la información deseada. Esto puede incluir la búsqueda de etiquetas HTML específicas y la 
#         extracción de datos de los atributos.
#
#      6. Almacenamiento de datos: Finalmente, se deben almacenar los datos extraídos en un formato adecuado, como un 
#         archivo CSV o una base de datos.
########################################################################################################################

class MySpider(scrapy.Spider):
    name = 'my_spider'

    start_urls = [
        'https://www.example.com',
    ]

    def getTitle(self, response):
        title = response.css('title::text').get()
        return title

    def getLink(self, response):
        link = response.css('a::attr(href)').get()
        return link

    def getAllLinks(self, response):
        links = response.css('a::attr(href)').getall()
        for link in links:
            print(f'Enlace: {link}')

    def parse(self, response):
        #######################################################################
        # Aquí puedes definir la lógica para extraer información del sitio web 
        # O si no, indicar pass para que no se realice ninguna acción.
        # pass
        #######################################################################
        print(self.getTitle(response))
        print(self.getLink(response))
        self.getAllLinks(response)