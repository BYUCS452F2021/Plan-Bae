# Date-Night-Planner Backend Server

## Running the server on your computer

### Initial Setup

This project requires at least Python 3.9, you'll want to make sure you're running that version on your local machine

If you haven't run the project before, navigate to the `backend` directory in your terminal and run:

* `pip install pipenv`
* `pipenv install`

If you're using VSCode, copy the Virtualenv location that was created by `pipenv install` (it will be displayed in the terminal output),  click on the bottom left of your VSCode project window (it will potentially say "Select Interpreter"), and past it in to the prompt. This will allow you to get type hints for this Python project.
### Subsequent Runs

Navigate to the `backend` directory in your terminal and run:

* `pipenv run dev`

You can visit [ localhost:5000/docs ]( http://localhost:5000/docs ) to test out the API as you write the code. If you'd prefer to use Postman, you can automatically import the API schema by using this URL to import the OpenAPI schema into Postman [ localhost:5000/openapi.json ]( http://localhost:5000/openapi.json ).

[text](https://link)
If you're curious what is going on behind the scenes when you run that command, open `Pipfile` and look up the command underneath the `[scripts]`  portion of file.