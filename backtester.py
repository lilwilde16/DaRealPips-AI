
import pandas as pd

def run_backtest(price_file, strategy_file):
    try:
        df = pd.read_csv(price_file)
        # Basic check
        if df.empty:
            return {"error": "Price data is empty."}

        # Simulate simple trade logic: buy if close > open
        df['result'] = df['close'] > df['open']
        win_rate = df['result'].mean()
        total_trades = len(df)
        return {
            "total_trades": total_trades,
            "win_rate": round(win_rate * 100, 2),
            "sample_strategy": strategy_file
        }
    except Exception as e:
        return {"error": str(e)}
