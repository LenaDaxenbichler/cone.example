#!/bin/bash

cd cone.app/src/cone/app/browser/static/scss/
sass style.scss ../style.css
sass light.scss ../light.css
sass dark.scss ../dark.css
cd ~/workspace/cone.example/
./bin/pserve example.ini
