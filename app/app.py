from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return jsonify({
            "message": "Company Domain Verification API"
    })

    @app.route("/health")
    def health_check():
        return jsonify({
            "status": "healthy"
    })

    return app



app = create_app()



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)