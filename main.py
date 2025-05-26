from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug = True) # automatically run when there are any changes. On on dev anad off during Prod
    