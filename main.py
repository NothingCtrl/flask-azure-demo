# -*- coding: utf-8 -*-
import os
from apps import app

if __name__ == "__main__":
    app.run(debug=os.getenv('DEBUG', 'False').lower() in ('true', '1'), host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

