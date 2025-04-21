import yfinance as yf

def compare_stocks(symbols):
    data = {}
    for symbol in symbols:
        try:
            stock = yf.Ticker(symbol)
            hist = stock.history(period="6mo")
            if hist.empty:
                continue
            data[symbol] = hist['Close'].pct_change().sum()
        except:
            continue
    return data

def get_company_info(symbol):
    stock = yf.Ticker(symbol)
    return {
        "name": stock.info.get("longName", "N/A"),
        "sector": stock.info.get("sector", "N/A"),
        "market_cap": stock.info.get("marketCap", "N/A"),
        "summary": stock.info.get("longBusinessSummary", "N/A"),
    }

def get_company_news(symbol):
    stock = yf.Ticker(symbol)
    return stock.news[:5]