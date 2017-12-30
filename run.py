#!/usr/bin/env python

from app import app
app.run(debug=True, host=app.config["LISTEN_HOST"])
