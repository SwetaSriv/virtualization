from flask import Flask, jsonify
import optuna

app = Flask(__name__)

def get_optuna_storage_url(port):
    return f'postgresql://optuna_user:optuna_password@optuna-db:{port + 5431}/optuna'

@app.route('/')
def hello():
    return 'Hello, this is the hyperparameter tuning service!'

@app.route('/tune_hyperparameters', methods=['GET'])
def tune_hyperparameters():
    port = int(request.host.split(":")[1])  # Extract port from request URL
    storage_url = get_optuna_storage_url(port)

    study_name = f'your_study_name_{port}'
    study = optuna.create_study(direction='maximize', study_name=study_name, storage=storage_url)
    
    study.optimize(objective, n_trials=100)
    best_params = study.best_params
    return jsonify(best_params)

def objective(trial):
    # Replace this with your actual machine learning model training and evaluation
    # Use trial.suggest_* to sample hyperparameters
    # Example:
    # learning_rate = trial.suggest_float('learning_rate', 1e-5, 1e-1, log=True)
    # dropout_rate = trial.suggest_float('dropout_rate', 0.0, 0.5)
    # ...

    # Mocking a simple objective function
    accuracy = trial.suggest_uniform('accuracy', 0.0, 1.0)
    return accuracy

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Adjust port if needed
