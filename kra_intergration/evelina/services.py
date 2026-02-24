def classify_user(user):
    if user.tax_paid > 10000 and user.net_pay > 0:
        user.role = 'DONOR'
        user.is_employed = True

    elif user.net_pay == 0:
        user.role = 'RECEIVER'
        user.is_employed = False

    else:
        user.role = 'UNCLASSIFIED'

    user.save()
