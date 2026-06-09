import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Global Market Cap Leaders",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Global Market Cap Leaders Dashboard")
st.caption("Yahoo Finance 데이터를 활용한 글로벌 시가총액 상위 기업 주가 비교")

# 글로벌 시총 상위 기업
TOP_COMPANIES = {
    "NVIDIA": "NVDA",
    "Microsoft": "MSFT",
    "Apple": "AAPL",
    "Alphabet": "GOOGL",
    "Amazon": "AMZN",
    "Broadcom": "AVGO",
    "TSMC": "TSM",
    "Meta": "META",
    "Berkshire Hathaway": "BRK-B",
    "Tesla": "TSLA"
}

col1, col2 = st.columns([2, 1])

with col1:
    selected = st.multiselect(
        "기업 선택",
        list(TOP_COMPANIES.keys()),
        default=[
            "NVIDIA",
            "Microsoft",
            "Apple",
            "Alphabet",
            "Amazon"
        ]
    )

with col2:
    period = st.selectbox(
        "조회 기간",
        ["1mo", "3mo", "6mo", "1y", "2y", "5y"],
        index=3
    )

normalize = st.toggle(
    "100 기준 수익률 비교",
    value=True
)

if selected:

    tickers = [TOP_COMPANIES[x] for x in selected]

    with st.spinner("Yahoo Finance 데이터 수집 중..."):
        df = yf.download(
            tickers=tickers,
            period=period,
            auto_adjust=True,
            progress=False
        )

    prices = df["Close"]

    if normalize:
        prices = prices.div(prices.iloc[0]).mul(100)

    chart_df = prices.reset_index()
    chart_df = chart_df.melt(
        id_vars="Date",
        var_name="Ticker",
        value_name="Price"
    )

    fig = px.line(
        chart_df,
        x="Date",
        y="Price",
        color="Ticker",
        template="plotly_white",
        title="Top Global Stocks Performance"
    )

    fig.update_layout(
        height=650,
        hovermode="x unified",
        legend_title="Ticker"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("📊 Performance Summary")

    perf = (
        prices.iloc[-1] / prices.iloc[0] - 1
    ) * 100

    summary = pd.DataFrame({
        "Ticker": perf.index,
        "Return (%)": perf.values.round(2)
    }).sort_values(
        "Return (%)",
        ascending=False
    )

    st.dataframe(
        summary,
        use_container_width=True
    )

    winner = summary.iloc[0]

    st.success(
        f"🏆 Best Performer: {winner['Ticker']} ({winner['Return (%)']}%)"
    )

else:
    st.warning("최소 1개 기업을 선택하세요.")
