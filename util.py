import sys
import yaml
import os.path
import QuantLib as ql
import pandas as pd

def get_configuration( configuration_filename : str ):

    if configuration_filename is None or os.path.exists(configuration_filename) is False:
        print("Configuration file {} is invalid".format(configuration_filename))
        sys.exit(1)

    with open(configuration_filename) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    return config


def get_config_by_key( configuration, key: str  ):
    
    for item in configuration:    
        if item == key:
            return configuration[item]


def determine_product_filter(product_params: list) -> str:
    
    product_filter_params = (
        f"symbol == '{product_params['name']}' and "
        f"{product_params['minExercisePrice']} < exercisePriceValue < {product_params['maxExercisePrice']} and "
        f"{product_params['minRateTime']} < rateTime < {product_params['maxRateTime']}" )
    
    print("Product Filter parameters are : {} ".format(product_filter_params))
    
    return product_filter_params      

#def determine_product_filter(product_params: list) -> str:
    if product_params['classCode'] == 'call':
        min_exercise_price = product_params['minExercisePriceCall']
        max_exercise_price = product_params['maxExercisePriceCall']
    elif product_params['classCode'] == 'put':
        min_exercise_price = product_params['minExercisePricePut']
        max_exercise_price = product_params['maxExercisePricePut']
    else:
        raise ValueError("Invalid classCode. Expected 'call' or 'put'.")

    product_filter_params = (
        f"symbol == '{product_params['name']}' and "
        f"{min_exercise_price} < exercisePriceValue < {max_exercise_price} and "
        f"{product_params['minRateTime']} < rateTime < {product_params['maxRateTime']}" )
    
    print("Product Filter parameters are : {} ".format(product_filter_params))

def extract_features(feature_params: list) -> str:
    feature_params_list = (
        f"'{feature_params['name']}' "
        f"{feature_params['minExercisePrice']} < exercisePriceValue < {feature_params['maxExercisePrice']} and "
        f"{feature_params['minRateTime']} < rateTime < {feature_params['maxRateTime']}"
    )
    
    #print("Product Filter parameters are : {} ".format(feature_params_list))
    
    return feature_params_list


def extract_keras_parameters(keras_model_params: list) -> list:
    
    return keras_model_params



''' '''

#configuration = get_configuration('./Configuration.yml')

#logLevel = configuration['logLevel']

#product_params = configuration['product']

#print(configuration['product']['name'])
#print(configuration['kerasModel']['inputLayer'])

#
#product_filter_params = determine_product_filter( get_config_by_key( configuration = configuration, key = 'product') )

#print("Product Filter parameters are : {}".format(product_filter_params) )
#print(product_params['minExercisePrice'])
#
#keras_model_params = extract_keras_parameters( get_config_by_key( configuration = configuration, key = 'kerasModel') )

#print("Keras Model parameters are : {}".format(keras_model_params) )