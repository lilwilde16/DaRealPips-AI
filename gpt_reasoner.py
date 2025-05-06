
def reason_trade(text):
    if "buy" in text.lower():
        return "This could be a valid buy if strength is rising and trend is positive."
    elif "sell" in text.lower():
        return "This may be a good sell if price is below moving average and strength is weak."
    else:
        return "Unable to determine reasoning without more context."
