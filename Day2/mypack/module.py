class Math:

    def even(num):
        if (num%2==0):
            return True
        return False

    def odd(num):
        if (num%2!=0):
            return True
        return False

    def isprime(num):
        for i in range(2,num):
            if (num%i==0):
                return False
        return True
    
    def power(base,exp):
        return base**exp
