# Cryptocurrency Research

This directory contains educational materials and research notebooks focused on cryptocurrency market analysis.

## Contents

### 1. Crypto_Herding_Measures.ipynb

A comprehensive notebook exploring herding behavior in cryptocurrency markets. This notebook covers:

**Theoretical Background:**
- Introduction to herding behavior in financial markets
- Why cryptocurrencies are particularly susceptible to herding
- Key academic literature and methodologies

**Herding Measures Implemented:**

1. **CSSD (Cross-Sectional Standard Deviation)** - Christie and Huang (1995)
   - Measures return dispersion during extreme market movements
   - Tests if dispersion decreases during market stress (evidence of herding)

2. **CSAD (Cross-Sectional Absolute Deviation)** - Chang, Cheng, and Khorana (2000)
   - More robust measure using absolute deviations
   - Tests for non-linear relationship between dispersion and market returns
   - Negative coefficient on squared market return indicates herding

3. **State-Dependent Herding Analysis**
   - Examines herding in different market conditions
   - Up vs Down markets
   - High vs Low volatility periods

**Features:**
- Complete implementation with Python code
- Simulated data examples (easily adaptable to real data)
- Statistical tests and interpretation guidelines
- Comprehensive visualizations
- Real-world data collection examples (yfinance, CoinGecko, Binance)

## Getting Started

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels
```

### For Real Data Collection

```bash
pip install yfinance pycoingecko ccxt
```

## Data Sources

The notebooks are designed to work with various cryptocurrency data sources:

1. **Yahoo Finance** (via yfinance) - Free, easy to use
2. **CoinGecko API** - Free tier available, no API key required
3. **CoinMarketCap API** - Requires free API key
4. **Binance API** - For high-frequency data
5. **CCXT Library** - Unified API for multiple exchanges

## Key References

### Herding Behavior Literature

1. **Christie, W.G., & Huang, R.D. (1995)**. "Following the Pied Piper: Do Individual Returns Herd around the Market?" *Financial Analysts Journal*, 51(4), 31-37.

2. **Chang, E.C., Cheng, J.W., & Khorana, A. (2000)**. "An examination of herd behavior in equity markets: An international perspective." *Journal of Banking & Finance*, 24(10), 1651-1679.

3. **Ballis, A., & Drakos, K. (2020)**. "Testing for herding in the cryptocurrency market." *Finance Research Letters*, 33, 101210.

4. **Bouri, E., Gupta, R., & Roubaud, D. (2019)**. "Herding behaviour in cryptocurrencies." *Finance Research Letters*, 29, 216-221.

5. **Vidal-Tomás, D., Ibáñez, A.M., & Farinós, J.E. (2019)**. "Herding in the cryptocurrency market: CSSD and CSAD approaches." *Finance Research Letters*, 30, 181-186.

## Understanding Herding in Crypto Markets

### Why Study Herding?

Herding behavior has important implications for:
- Market efficiency
- Price discovery
- Risk management
- Portfolio diversification
- Regulatory policy

### Cryptocurrency-Specific Factors

Cryptocurrencies exhibit unique characteristics that may amplify herding:

1. **Retail Dominance**: High proportion of retail investors who may be more prone to herding
2. **Social Media Influence**: Twitter, Reddit, Telegram groups drive collective behavior
3. **Influencer Impact**: Major figures (e.g., Elon Musk) can trigger herd movements
4. **Information Asymmetry**: Limited fundamental analysis tools compared to traditional assets
5. **Market Immaturity**: Young markets with less institutional stabilization
6. **24/7 Trading**: Continuous trading may amplify momentum effects
7. **FOMO Culture**: Fear of missing out drives speculative behavior

## Practical Applications

### For Traders
- Identify periods of excessive herding for contrarian strategies
- Understand market vulnerability during extreme movements
- Improve entry/exit timing

### For Risk Managers
- Assess systemic risk from collective behavior
- Model tail risk scenarios
- Develop stress testing frameworks

### For Researchers
- Extend analysis to specific cryptocurrency categories (DeFi, NFTs, memecoins)
- Incorporate sentiment analysis and on-chain metrics
- Study cross-market herding (crypto-equity spillovers)

## Future Extensions

Potential areas for further research:

1. **Sentiment Integration**: Incorporate Twitter sentiment, Google Trends, Fear & Greed Index
2. **On-Chain Metrics**: Use blockchain data (active addresses, transaction volumes)
3. **Network Analysis**: Examine herding across related cryptocurrencies
4. **High-Frequency Analysis**: Minute-level or tick data for intraday herding
5. **Machine Learning**: Predict herding episodes using ML models
6. **Cross-Asset Herding**: Study spillovers between crypto and traditional markets
7. **Category-Specific Analysis**: DeFi tokens, stablecoins, NFT-related tokens

## Contributing

If you find errors or have suggestions for improvements, please reach out!

## License

These materials are provided for educational purposes.

---

**Last Updated**: January 2026
