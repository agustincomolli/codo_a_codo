from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from flask_cors import CORS

# Configurar la aplicación Flask
app = Flask(__name__)

# Esto permite a todas las rutas aceptar solicitudes de origen cruzado. Para
# producción, deberías limitar esto a orígenes conocidos.
CORS(app)


def get_database_uri():
    # Configuración de la base de datos
    user = 'root'
    password = 'eggh-22cgFb-gBg4aH6DfFAC14edeFC6'
    db_name = 'railway'
    host = 'viaduct.proxy.rlwy.net'
    port = 51991

    return f'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}'


app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db = SQLAlchemy(app)


class ProductModel(db.Model):
    """
    Modelo SQLAlchemy para la tabla de productos.
    """
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)


class Product:
    """
    Clase Producto para manejar las conexiones de la base de datos y las operaciones CRUD de los productos.
    """

    def __init__(self):
        self.my_product = ProductModel()

    @staticmethod
    def setup_database():
        """
        Método para configurar la base de datos.
        """
        with app.app_context():
            db.create_all()  # Crear tablas en la base de datos si no existen

    def add_product(self, name, price, stock):
        """
        Método para agregar un producto a la base de datos.
        """
        with app.app_context():
            new_product = ProductModel(name=name, price=price, stock=stock)
            db.session.add(new_product)
            db.session.commit()

    def delete_product(self, product_id):
        """
        Método para eliminar un producto de la base de datos.
        """
        with app.app_context():
            product = ProductModel.query.get(product_id)
            if product:
                db.session.delete(product)
                db.session.commit()

    def modify_product(self, product_id, name=None, price=None, stock=None):
        """
        Método para modificar un producto en la base de datos.
        """
        with app.app_context():
            product = ProductModel.query.get(product_id)
            if product:
                if name is not None:
                    product.name = name
                if price is not None:
                    product.price = price
                if stock is not None:
                    product.stock = stock

                db.session.commit()

    def get_product(self, product_id):
        """
        Método para obtener un producto de la base de datos.
        """
        with app.app_context():
            product = ProductModel.query.get(product_id)
            return product


@app.route("/products", methods=["POST"])
def add_product():
    """
    Añadir un producto a través de una petición y devolver un mensaje.
    """
    name = request.form["name"]
    price = request.form["price"]
    stock = request.form["stock"]

    try:
        with app.app_context():
            new_product = ProductModel(name=name, price=price, stock=stock)
            db.session.add(new_product)
            db.session.commit()
        return jsonify({"message": "Producto agregado"})
    except:
        return jsonify({"message": "No se ha podido agregar el producto"})


@app.route("/products", methods=["GET"])
def get_products():
    """
    Obtener todos los productos de la base de datos y devolverlos en una respuesta JSON.
    """
    with app.app_context():
        products = ProductModel.query.all()  # Obtener todos los productos
        product_list = [
            {"id": product.id, "name": product.name, "price": str(
                product.price), "stock": product.stock}
            for product in products
        ]  # Crear una lista de diccionarios con los datos de los productos

        # Devuelve la lista de productos como JSON
        return jsonify(product_list)


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """
    Eliminar un producto por su ID de la base de datos y devolver un mensaje.
    """
    # Crea una sesión a tu base de datos
    with Session(bind=db.engine) as session:
        # Usa la nueva forma recomendada para obtener el producto
        product = session.get(ProductModel, product_id)
        # Si no encuentra el producto, devuelve un error
        if product is None:
            return jsonify({"message": "Producto no encontrado"}), 404

        # Proceder a eliminar el producto
        try:
            session.delete(product)
            session.commit()
            return jsonify({"message": "Producto eliminado"}), 200
        except Exception as e:
            # Algún error ocurrió, como un error de base de datos
            session.rollback()
            return jsonify({"message": f"Error al eliminar el producto: {str(e)}"}), 500


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product():
    pass

if __name__ == "__main__":
    Product.setup_database()
    app.run(host="0.0.0.0", debug=True)
