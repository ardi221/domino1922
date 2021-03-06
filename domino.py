# higgsdomino-- options
local scriptName = [=====[Script for Higgs Domino 1.64]=====]
local scriptVersion = '1.0.0'
local scriptAuthor = 'User'
local startToast = ''
-- 0 - no check; 1 - check package only, 2 - check package and build
local checkTarget = 0

local targetName = [=====[Higgs Domino]=====]
local targetPkg = 'com.neptune.domino'
local targetVersion = [=====[1.64]=====]
local targetBuild = 1641

-- functions

-- init
gg.require('101.0', 16139)
gg.toast("DuoFu DuoCai Cheat By L3n4r0x")

-- mini reward
gg.toast('tweak mini reward')
gg.clearResults()
gg.searchNumber("800000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("176000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("1800000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("176000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("3800000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("176000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("6800000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("176000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("8800000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("176000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("17600000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("176000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("44000000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("176000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("61600000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("176000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("88000000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("176000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("132000000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("176000000", gg.TYPE_DWORD)

-- minor
gg.toast('tweak minor reward')

gg.clearResults()
gg.searchNumber("2000000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("440000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("4500000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("440000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("9500000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("440000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("17000000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("440000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("22000000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("440000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("44000000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("440000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("110000000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("440000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("154000000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("440000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("220000000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("440000000", gg.TYPE_DWORD)

gg.clearResults()
gg.searchNumber("330000000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("440000000", gg.TYPE_DWORD)

-- major

-- small reward
gg.clearResults()
gg.searchNumber("150000", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("15000000", gg.TYPE_DWORD)
gg.processResume()

gg.clearResults()
gg.searchNumber("100000", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.timeJump("1:1:0")
gg.searchFuzzy("0", gg.SIGN_FUZZY_EQUAL, gg.TYPE_DWORD | gg.TYPE_XOR | gg.TYPE_FLOAT | gg.TYPE_QWORD | gg.TYPE_DOUBLE, 0, -1, 0)
gg.editAll("10000000", gg.TYPE_DWORD)
gg.processResume()

gg.clearResults()
gg.searchNumber("50000", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("5000000", gg.TYPE_DWORD)
gg.processResume()
gg.refineNumber("50000", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
