# -*- coding: utf-8 -*-
import os
import time
from pathlib import Path
from flask import Flask
import logging

app_start_time = int(time.time())
_logger = logging.getLogger(__name__)
_logger.info("App start time: {}".format(app_start_time))

_path = Path(os.path.realpath(__file__))
base_dir = os.path.dirname(_path.parent.absolute())

app = Flask(__name__,
            template_folder=os.path.join(base_dir, 'templates'),
            static_folder=os.path.join(base_dir, 'static'))
