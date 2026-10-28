# Shared f_tools() for BOARD generators — 9-tuple compatible with أفضل فرص f_opp

F_TOOLS_BOARD = '''
f_tools() =>
    float ema20 = ta.ema(close, 20)
    float ema50 = ta.ema(close, 50)
    float ema200 = ta.ema(close, 200)
    float rsi = ta.rsi(close, 14)
    [macdL, macdS, macdH] = ta.macd(close, 12, 26, 9)
    float volMa = ta.sma(volume, 20)
    bool liq = volMa >= minVol
    float rvol = volume / math.max(volMa, 1.0)
    float rng = math.max(high - low, syminfo.mintick)
    float cmf = ta.sma(((close - low) - (high - close)) / rng * volume, 20) / ta.sma(volume, 20)
    float obvSl = ta.linreg(ta.obv, 10, 0) - ta.linreg(ta.obv, 10, 1)
    [diP, diM, adx] = ta.dmi(14, 14)
    [stLine, stDir] = ta.supertrend(3.0, 10)
    float lookHi = ta.highest(high, 80)
    float lookLo = ta.lowest(low, 80)
    bool inDem = close <= lookHi - 0.618 * (lookHi - lookLo) and close >= lookLo
    bool bosUp = close > ta.highest(high, 20)[1]
    float hi = ta.highest(high, 252)
    bool chase = hi > 0 and (close - hi) / hi * 100.0 > -3 and rsi > 72
    float dPrev = close[1]
    float dayPct = dPrev > 0 ? (close - dPrev) / dPrev * 100.0 : 0.0
    float haltPct = egxBoard == "SME تميّز" or egxBoard == "SME نايل" or egxBoard == "غير نشط" ? 5.0 : 10.0
    float luldPct = egxBoard == "غير نشط" ? 5.0 : (egxBoard == "SME تميّز" or egxBoard == "SME نايل" ? 10.0 : 20.0)
    bool nearLimit = dayPct >= math.min(9.0, haltPct - 1.0) or dayPct >= luldPct - 0.25
    int v01 = rsi > 52 and rsi < 68 ? 1 : rsi >= 68 ? 0 : -1
    int v02 = macdH > 0 and macdL > macdS ? 1 : macdH < 0 ? -1 : 0
    int v03 = ta.stoch(close, high, low, 14) > 50 ? 1 : -1
    int v04 = ta.roc(close, 10) > 0 ? 1 : -1
    int v05 = ta.mfi(hlc3, 14) > 50 ? 1 : -1
    int v06 = adx > 22 and diP > diM ? 1 : adx > 22 and diM > diP ? -1 : 0
    int v07 = close > ema20 and ema20 > ema50 and ema50 > ema200 ? 1 : close < ema20 and ema20 < ema50 ? -1 : 0
    int v08 = stDir < 0 ? 1 : -1
    int v10 = cmf > 0.05 ? 1 : cmf < -0.05 ? -1 : 0
    int v11 = obvSl > 0 ? 1 : obvSl < 0 ? -1 : 0
    int v12 = ta.accdist > ta.ema(ta.accdist, 20) ? 1 : -1
    int v15 = bosUp ? 1 : close < ta.lowest(low, 20)[1] ? -1 : 0
    int v16 = inDem ? 1 : close > lookHi * 0.98 ? -1 : 0
    int sumV = v01 + v02 + v03 + v04 + v05 + v06 + v07 + v08 + v10 + v11 + v12 + v15 + v16
    float score = sumV / 13.0 * 100.0
    int nG = (v01 == 1 ? 1 : 0) + (v02 == 1 ? 1 : 0) + (v03 == 1 ? 1 : 0) + (v04 == 1 ? 1 : 0) + (v05 == 1 ? 1 : 0) + (v06 == 1 ? 1 : 0) + (v07 == 1 ? 1 : 0) + (v08 == 1 ? 1 : 0) + (v10 == 1 ? 1 : 0) + (v11 == 1 ? 1 : 0) + (v12 == 1 ? 1 : 0) + (v15 == 1 ? 1 : 0) + (v16 == 1 ? 1 : 0)
    int nR = (v01 == -1 ? 1 : 0) + (v02 == -1 ? 1 : 0) + (v03 == -1 ? 1 : 0) + (v04 == -1 ? 1 : 0) + (v05 == -1 ? 1 : 0) + (v06 == -1 ? 1 : 0) + (v07 == -1 ? 1 : 0) + (v08 == -1 ? 1 : 0) + (v10 == -1 ? 1 : 0) + (v11 == -1 ? 1 : 0) + (v12 == -1 ? 1 : 0) + (v15 == -1 ? 1 : 0) + (v16 == -1 ? 1 : 0)
    bool locOK = inDem or bosUp or v16 == 1
    bool moneyOK = v10 == 1 and v11 != -1 and v12 == 1
    bool upTrend = v07 == 1 or v08 == 1
    bool momOK = score >= sigMin * 0.5
    bool trigOK = close > open and (v03 == 1 or v04 == 1)
    bool volOK = rvol >= 0.9
    int hits = (upTrend ? 1 : 0) + (locOK ? 1 : 0) + (momOK ? 1 : 0) + (moneyOK ? 1 : 0) + (trigOK ? 1 : 0) + (volOK ? 1 : 0)
    bool egxOK = liq and not chase and not nearLimit
    bool buyA = egxOK and locOK and moneyOK and hits >= 5 and score >= sigMin
    bool buyB = egxOK and locOK and not buyA and hits >= 4 and score >= sigMin * 0.5
    bool buy = buyA or buyB
    float accSc = nG / 13.0 * 100.0
    float distSc = nR / 13.0 * 100.0
    float atr = ta.atr(14)
    float pl = ta.pivotlow(low, 8, 8)
    var float sl = na
    if not na(pl)
        sl := pl
    float ph = ta.pivothigh(high, 8, 8)
    var float sh = na
    if not na(ph)
        sh := ph
    float zw = atr * 0.35
    float t1 = na(sh) ? close + atr * 1.5 : sh
    float stopPx = nz(sl, close) - zw * 1.2 - atr * 0.5
    float entryPx = close
    float rr = math.max(entryPx - stopPx, syminfo.mintick) > 0 ? (t1 - entryPx) / math.max(entryPx - stopPx, syminfo.mintick) : 0.0
    float roc20 = ta.roc(close, 20)
    [score, buy ? 1.0 : 0.0, hits, rvol, roc20, accSc, distSc, rr, dayPct]
'''

# Legacy 10-tuple for simple board script
F_TOOLS = F_TOOLS_BOARD

# 17-tuple compatible with EGX_افضل_فرص_BOARD200 f_opp → f_cache
F_TOOLS_BOARD_FULL = '''
f_tools() =>
    bool sigOk = not confirmClose or barstate.isconfirmed
    float ema20 = ta.ema(close, 20)
    float ema50 = ta.ema(close, 50)
    float ema200 = ta.ema(close, 200)
    float rsi = ta.rsi(close, 14)
    [macdL, macdS, macdH] = ta.macd(close, 12, 26, 9)
    float volMa = ta.sma(volume, 20)
    bool liqOk = volMa >= effMinVol
    float rvol = volume / math.max(volMa, 1.0)
    float rng = math.max(high - low, syminfo.mintick)
    float cmf = ta.sma(((close - low) - (high - close)) / rng * volume, 20) / ta.sma(volume, 20)
    float obvSl = ta.linreg(ta.obv, 10, 0) - ta.linreg(ta.obv, 10, 1)
    [diP, diM, adx] = ta.dmi(14, 14)
    [_, stDir] = ta.supertrend(3.0, 10)
    float lookHi = ta.highest(high, 80)
    float lookLo = ta.lowest(low, 80)
    bool inDem = close <= lookHi - 0.618 * (lookHi - lookLo) and close >= lookLo
    bool bosUp = close > ta.highest(high, 20)[1]
    float hi252 = ta.highest(high, 252)
    bool chase = hi252 > 0 and (close - hi252) / hi252 * 100.0 > -3.0 and rsi > 72
    float dPrev = close[1]
    float dayPct = dPrev > 0 ? (close - dPrev) / dPrev * 100.0 : 0.0
    float haltPct = egxBoard == "SME تميّز" or egxBoard == "SME نايل" or egxBoard == "غير نشط" ? 5.0 : 10.0
    float luldPct = egxBoard == "غير نشط" ? 5.0 : (egxBoard == "SME تميّز" or egxBoard == "SME نايل" ? 10.0 : 20.0)
    bool nearLimit = blockLimit and dPrev > 0 and (dayPct >= math.min(9.0, haltPct - 1.0) or dayPct >= luldPct - 0.25)
    int v01 = rsi > 52 and rsi < 68 ? 1 : rsi >= 68 ? 0 : -1
    int v02 = macdH > 0 and macdL > macdS ? 1 : macdH < 0 ? -1 : 0
    int v03 = ta.stoch(close, high, low, 14) > 50 ? 1 : -1
    int v04 = ta.roc(close, 10) > 0 ? 1 : -1
    int v05 = ta.mfi(hlc3, 14) > 50 ? 1 : -1
    int v06 = adx > 22 and diP > diM ? 1 : adx > 22 and diM > diP ? -1 : 0
    int v07 = close > ema20 and ema20 > ema50 and ema50 > ema200 ? 1 : close < ema20 and ema20 < ema50 ? -1 : 0
    int v08 = stDir < 0 ? 1 : -1
    int v10 = cmf > 0.05 ? 1 : cmf < -0.05 ? -1 : 0
    int v11 = obvSl > 0 ? 1 : obvSl < 0 ? -1 : 0
    int v12 = ta.accdist > ta.ema(ta.accdist, 20) ? 1 : -1
    int v15 = bosUp ? 1 : close < ta.lowest(low, 20)[1] ? -1 : 0
    int v16 = inDem ? 1 : close > lookHi * 0.98 ? -1 : 0
    float tech = (v01 + v02 + v03 + v04 + v05 + v06 + v07 + v08 + v10 + v11 + v12 + v15 + v16) / 13.0 * 100.0
    int nG = (v01 == 1 ? 1 : 0) + (v02 == 1 ? 1 : 0) + (v03 == 1 ? 1 : 0) + (v04 == 1 ? 1 : 0) + (v05 == 1 ? 1 : 0) + (v06 == 1 ? 1 : 0) + (v07 == 1 ? 1 : 0) + (v08 == 1 ? 1 : 0) + (v10 == 1 ? 1 : 0) + (v11 == 1 ? 1 : 0) + (v12 == 1 ? 1 : 0) + (v15 == 1 ? 1 : 0) + (v16 == 1 ? 1 : 0)
    int nR = (v01 == -1 ? 1 : 0) + (v02 == -1 ? 1 : 0) + (v03 == -1 ? 1 : 0) + (v04 == -1 ? 1 : 0) + (v05 == -1 ? 1 : 0) + (v06 == -1 ? 1 : 0) + (v07 == -1 ? 1 : 0) + (v08 == -1 ? 1 : 0) + (v10 == -1 ? 1 : 0) + (v11 == -1 ? 1 : 0) + (v12 == -1 ? 1 : 0) + (v15 == -1 ? 1 : 0) + (v16 == -1 ? 1 : 0)
    float accScore = nG / 13.0 * 100.0
    float distRisk = nR / 13.0 * 100.0
    bool locOK = inDem or bosUp or v16 == 1
    bool moneyOK = v10 == 1 and v11 != -1 and v12 == 1
    bool upTrend = v07 == 1 or v08 == 1
    bool momOK = tech >= sigMin * 0.5
    bool trigOK = close > open and (v03 == 1 or v04 == 1)
    bool volOK = rvol >= 0.9
    int setupHits = (upTrend ? 1 : 0) + (locOK ? 1 : 0) + (momOK ? 1 : 0) + (moneyOK ? 1 : 0) + (trigOK ? 1 : 0) + (volOK ? 1 : 0)
    float pl = ta.pivotlow(low, 8, 8)
    var float swingLow = na
    if not na(pl)
        swingLow := pl
    bool supportBreak = sigOk and not na(swingLow) and close < swingLow and close[1] >= swingLow
    float atr = ta.atr(14)
    float zw = atr * 0.35
    bool nearSupport = not na(swingLow) and low <= nz(swingLow, low) + zw and close >= nz(swingLow, low) - zw * 1.2
    float ph = ta.pivothigh(high, 8, 8)
    var float swingHigh = na
    if not na(ph)
        swingHigh := ph
    float t1 = na(swingHigh) ? close + atr * 1.5 : swingHigh
    float entryPx = close
    float stopPx = nz(swingLow, close) - zw * 1.2 - atr * 0.5
    float riskPx = math.max(entryPx - stopPx, syminfo.mintick)
    float rr = riskPx > 0 ? (t1 - entryPx) / riskPx : 0.0
    float roc20 = ta.roc(close, 20)
    float benchRocL = request.security(bench, "D", ta.roc(close, 20), barmerge.gaps_off, barmerge.lookahead_off)
    bool rsLeader = roc20 - benchRocL > 0
    setupHits += rsLeader ? 1 : 0
    float rank = math.max(0.0, math.min(100.0, tech * 0.55 + setupHits / 7.0 * 30.0 + (rsLeader ? 8.0 : 0.0) + (rvol >= 1.2 ? 7.0 : 0.0)))
    float opportunity = math.max(0.0, math.min(100.0, tech * 0.55 + setupHits / 7.0 * 100.0 * 0.35 + math.min(100.0, rr / 3.0 * 100.0) * 0.15 + (rsLeader ? 5.0 : 0.0)))
    bool chaseOk = not blockChase or not chase
    bool buyRaw = sigOk and liqOk and not supportBreak and setupHits >= effMinSetup and rr >= minRR and (nearSupport or bosUp or inDem) and tech >= sigMin and chaseOk and not nearLimit and distRisk < 65
    bool passRaw = buyRaw and rank >= effMinRank and opportunity >= 58.0
    bool proRaw = passRaw and opportunity >= effMinOppScr and setupHits >= 6 and accScore >= 45 and distRisk < 50
    int cycle12 = distRisk >= 55 ? 9 : supportBreak ? 11 : accScore >= 55 and nearSupport ? 4 : bosUp ? 6 : 3
    int action = supportBreak or nearLimit ? 0 : proRaw or buyRaw ? 3 : passRaw or (setupHits >= 6 and opportunity >= 58) ? 2 : 1
    [opportunity, rank, tech, buyRaw ? 1.0 : 0.0, passRaw ? 1.0 : 0.0, proRaw ? 1.0 : 0.0, setupHits, rvol, roc20, accScore, distRisk, rr, dayPct, action, cycle12, chase ? 1.0 : 0.0, nearLimit ? 1.0 : 0.0]
'''
