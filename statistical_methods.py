class Statistics:

    @staticmethod
    def percentage_difference(a,b):
        a = float(a)
        b = float(b)

        answer = (abs(a-b) / ((a+b)/2)) * 100
        return f'{round(answer,2)}%'

    @staticmethod
    def percentage_change(new_value, old_value):
        new_value = float(new_value)
        old_value = float(old_value)

        answer =  ((new_value-old_value)/old_value) * 100
        return f'{round(answer,2)}%'

    @staticmethod
    def pearson_correlation_explain(r):
        if not -1 <= r <= 1:
            return 'Invalid input: Correlation Coefficient must be between -1 and 1'

        print(f'The pearson correlation coefficient is: {round(r, 3)}')

        if r == 1:
            return 'Perfect positive correlation: Variables increase together with a perfect linear relationship.'

        elif r == -1:
            return 'Perfect negative correlation: As one variable increases, the other decreases with a perfect linear relationship.'

        elif 0.7 <= r < 1:
            return 'Strong positive correlation: As one variable increases, the other tends to increase significantly.'

        elif -1 < r <= -0.7:
            return 'Strong negative correlation: As one variable increases, the other tends to decrease significantly.'

        elif 0.4 <= r < 0.7:
            return 'Moderate positive correlation: There is a noticeable positive relationship between the variables.'

        elif -0.7 < r <= -0.4:
            return 'Moderate negative correlation: There is a noticeable negative relationship between the variables.'

        elif 0.1 <= r < 0.4:
            return 'Weak positive correlation: A slight tendency for one variable to increase when the other does.'

        elif -0.4 < r <= -0.1:
            return 'Weak negative correlation: A slight tendency for one variable to decrease when the other increases.'

        else:
            return 'Very weak or no correlation: The variables do not have a meaningful linear relationship.'