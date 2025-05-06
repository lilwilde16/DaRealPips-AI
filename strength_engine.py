
import pandas as pd

def get_strength_data(price_file):
    try:
        df = pd.read_csv(price_file)
        if df.empty:
            return {"error": "No data."}

        df['volatility'] = df['high'] - df['low']
        df['trend'] = df['close'] - df['open']
        df['strength'] = df['volatility'] + abs(df['trend'])

        return df[['datetime', 'volatility', 'trend', 'strength']].tail(20)
    except Exception as e:
        return {"error": str(e)}
