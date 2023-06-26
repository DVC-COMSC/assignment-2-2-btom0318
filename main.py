def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    celcius = float(input("Enter a temperature in celcuis:  "))
    fahrenheit = (9/5)*celcius+32
    print (celcius)
    print (f' Temperature converted to fahrenheit \t {fahrenheit: .2f}')
        

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
