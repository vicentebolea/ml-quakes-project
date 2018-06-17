# RAPID EARTHQUAKE EARLY WARNING SYSTEM MACHINE LEARNING FRAMEWORK
This work implements four different deep learning model to predict:

  1. The arrival of the S-wave in a four different locations.
  2. The magnitude of the S-wave.
  3. The epicenter.
  4. The depth of the earthquake.

Based on the following independent variable:
  1. Ten different detecting stations's locations.
  2. Ten different detecting stations's P-wave arrival time.

## REQUIREMENTS
  1. Having a dedicated NVIDIA GPU

## INSTALLING

    $ pip install --user pipenv
    $ pipenv install --skip-lock

## RUNNING IT

    $ pipenv run python ./driver.py

## AUTHORS

Hero                         | email
-----------------------------|-------------------------
Vicente Adolfo Bolea Sanchez | <vicente.bolea@gmail.com>
Olzhas Kaiyrakhmet           | olzhabay.i@gmail.com>
