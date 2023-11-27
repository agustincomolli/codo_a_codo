from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Configurar la aplicación Flask
app = Flask(__name__)


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


@app.route("/products", methods=["post"])
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


if __name__ == "__main__":
    Product.setup_database()
    app.run(host="0.0.0.0", debug=True)
