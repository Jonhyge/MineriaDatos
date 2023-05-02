import pandas as pd
import datetime

def Practica_2():
    df = pd.read_csv("Google-Playstore.csv")
    df = df.drop(['Scraped Time'], axis=1)
    df = df.drop(['Minimum Installs'], axis=1)
    df['Category'] = df['Category'].replace(to_replace=["Adventure", "Tools", "Communication", "Racing", "Entertainment", "Photography", "Libraries & Demo",
                                                        "Food & Drink", "Medical", "Books & Reference", "Maps & Navigation", "Travel & Local", "Auto & Vehicles",
                                                        "Lifestyle", "Health & Fitness", "Music & Audio", "Finance", "News & Magazines", "Productivity", "Art & Design",
                                                        "Beauty", "Sports", "Business", "Events", "Weather", "Strategy", "Action", "Dating", "Educational",
                                                        "House & Home", "Music", "Parenting", "Role Playing", "Video Players & Editors", "Education"],
                                            value=["Aventura", "Herramientas", "Comunicacion", "Carreras", "Entretenimiento", "Fotografia", "Librerias y Demo",
                                                   "Comida y Bebidas", "Medico", "Libros y Referencias", "Mapas y navegacion", "Viaje y Local",
                                                   "Automoviles y vehiculos", "Estilo de vida", "Salud y Fisico", "Audio y Musica", "Finanzas",
                                                   "Noticias  y  Revistas", "Productividad", "Diseño y Arte", "Belleza", "Deportes", "Negocios", "Eventos", "Clima",
                                                   "Estrategia", "Accion", "Citas", "Educacionales", "Casa y Hogar", "Musica", "Paternidad", "Juegos de Rol",
                                                   "Editores de Video", "Educacion"])
    df['Content Rating'] = df['Content Rating'].replace(to_replace=["Teen", "Everyone", "Mature 17+"], value=["Jovenes", "Para todos", "Mayores 17"])
    df.columns = ['Nombre de la App', 'ID', 'Categoria', 'Rating', 'Cantidad Rating', 'Instalaciones', 'Maximo Instalaciones', 'Gratuito', 'Precio', 'Moneda', 'Tamaño de App',
                 'Version Android minima', 'ID del Desarrollador', 'Pagina Web del Desarrollador', 'Correo del Desarrollador', 'Fecha de lanzamiento', 'Ultima actualizacion',
                 'Rating de contenido','Politicas de privacidad', 'Contiene anuncios', 'Contiene compras', 'Editors Choice']
    fecha = pd.DatetimeIndex(df['Fecha de lanzamiento']).year
    df['Año de lanzamiento'] = fecha
    df = df.drop(['Fecha de lanzamiento'], axis=1)


    df.to_csv('Play_Store_Apps_limpio.csv', index=False)


Practica_2()