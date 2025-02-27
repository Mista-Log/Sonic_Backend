# Sonic Backend

This is the backend for the Sonic project, built using Solana.

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python (v3.8 or higher)
- pip
- Solana CLI

### Steps

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Mista-Log/Sonic_Backend
    cd sonic_backend
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    On Windows:
    ```sh
    .\venv\Scripts\activate
    ```
    On macOS and Linux:
    ```sh
    source venv/bin/activate
    ```

4. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

5. **Set up environment variables:**

    Create a `.env` file in the root directory and add the necessary environment variables. Refer to `.env.example` for the required variables.

6. **Run migrations:**

    ```sh
    python manage.py migrate
    ```

7. **Start the development server:**

    ```sh
    python manage.py runserver
    ```

### Testing

To run tests, use the following command:

```sh
python -m unittest discover
```

### Deployment

For deployment instructions, refer to the [Deployment Guide](./DEPLOYMENT.md).

## Contributing

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Environment Setup

To install and activate the environment, follow these steps:

1. **Install virtual environment package:**

    ```sh
    pip install virtualenv
    ```

2. **Create and activate the virtual environment:**

    ```sh
    virtualenv venv
    source venv/bin/activate
    ```