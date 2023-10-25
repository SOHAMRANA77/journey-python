#!/usr/bin/env python3

# Simple "How many days assuming I do dailies and use all my resin (180 per day) I need until AR X"
# This only works starting from AR35

# fill out these variables (current ones are mine :D)
MY_AR_EXP = 57726
MY_AR = 57
WANTED_AR = 58
# for the whales: Assuming you refill resin with primogems. Up to 6 times per day
PRIMOGEM_REFILLS_PER_DAY = 80

######################################################
# ignore everything after this just hit "Run"
######################################################
ADVENTURE_RANK_EXP_TABLE = {
    35: 105150,
    36: 112625,
    37: 120375,
    38: 128425,
    39: 136750,
    40: 145375,
    41: 155925,
    42: 167450,
    43: 179925,
    44: 193375,
    45: 207775,
    46: 223125,
    47: 239450,
    48: 256725,
    49: 274975,
    50: 294175,
    51: 320575,
    52: 349375,
    53: 380575,
    54: 414175,
    55: 450175,
    56: 682525,
    57: 941475,
    58: 1227225,
    59: 1540050,
    60: 1880175,
}

RESIN_USAGE_PER_DAY = 180
EXP_PER_20_RESIN = 100

RESIN_EXP_PER_DAY = RESIN_USAGE_PER_DAY / 20 * EXP_PER_20_RESIN
DAILY_COMMISION_EXP = 500 + (4 * 250)
#PRIMOGEM_EXP_PER_DAY = max(min(PRIMOGEM_REFILLS_PER_DAY, 6), 0) * (3 * EXP_PER_20_RESIN)

EXP_GAIN_PER_DAY = DAILY_COMMISION_EXP + RESIN_EXP_PER_DAY #+ PRIMOGEM_EXP_PER_DAY
TOTAL_EXP_REQUIRED = ADVENTURE_RANK_EXP_TABLE[WANTED_AR] - ADVENTURE_RANK_EXP_TABLE[MY_AR] - MY_AR_EXP

print("Current AR:", MY_AR, "Exp:", MY_AR_EXP)
print("Total Exp required:", TOTAL_EXP_REQUIRED)

print("Est. days until AR", str(WANTED_AR) + ",", TOTAL_EXP_REQUIRED / EXP_GAIN_PER_DAY)
k = (TOTAL_EXP_REQUIRED / EXP_GAIN_PER_DAY)/30
print("Est. Months until AR", str(WANTED_AR) + ",", k)