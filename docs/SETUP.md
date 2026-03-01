# Setup Guide for NeuroGuardAI

## Backend Setup

1. **Clone the Repository**  
   Clone the NeuroGuardAI repository to your local machine:
   ```bash
   git clone https://github.com/kumaran852/NeuroGuardAI.git
   cd NeuroGuardAI
   ```

2. **Set Up Python Environment**  
   Ensure you have Python 3.8 or higher installed. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**  
   Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**  
   Copy the example environment file and update your variables:
   ```bash
   cp .env.example .env
   nano .env  # or any text editor
   ```

5. **Run Migrations**  
   Prepare the database by running migrations:
   ```bash
   python manage.py migrate
   ```

6. **Start the Backend Server**  
   Run the server:
   ```bash
   python manage.py runserver
   ```
   Your backend should now be running at `http://127.0.0.1:8000`.

## Android Setup

1. **Install Android Studio**  
   Download and install [Android Studio](https://developer.android.com/studio).

2. **Clone the Repository**  
   If you haven't done so already, clone the NeuroGuardAI repository:
   ```bash
   git clone https://github.com/kumaran852/NeuroGuardAI.git
   cd NeuroGuardAI
   ```

3. **Open the Project in Android Studio**  
   Launch Android Studio and select `Open an existing Android Studio project`. Navigate to the cloned repository and select the project folder.

4. **Sync Gradle**  
   Allow Gradle to sync the project. It will download necessary dependencies based on the `build.gradle` files.

5. **Run the App**  
   Connect your Android device or start an emulator. Click on the `Run` icon in Android Studio to launch the app on your device or emulator.

6. **Configure API Endpoints**  
   Ensure that the app's configuration points to the backend server you set up earlier, typically found in the `build.gradle` or a config file.

## Conclusion
You now have the backend and Android application set up! For further configurations and explorations, please refer to the project's documentation and source code.