import pytest
from audio import adaptive_music as mod

CASES = [
    ("clock_one", "m.sample_clock(1, 60, 48000) == 800"),
    ("clock_second", "m.sample_clock(2, 60, 48000) == 1600"),
    ("bar_one", "m.bar_quantize(2.5, 120, 4) == approx(2.0)"),
    ("bar_zero", "m.bar_quantize(0.0, 120, 4) == approx(0.0)"),
    ("power_half", "m.equal_power(0.5) == approx(2 ** 0.5 / 2)"),
    ("power_zero", "m.equal_power(0.0) == approx(0.0)"),
    ("power_one", "m.equal_power(1.0) == approx(1.0)"),
    ("hyst_high", "m.hysteresis(1.0, 0.5, False) is True"),
    ("hyst_low", "m.hysteresis(0.0, 0.5, True) is False"),
    ("preload_yes", "m.preload_ready(3, 2) is True"),
    ("preload_no", "m.preload_ready(1, 2) is False"),
    ("loop_zero", "m.loop_align(5, 4) == 1"),
    ("pause_on", "m.pause_clock(100, True) == 0"),
    ("pause_off", "m.pause_clock(100, False) == 100"),
    ("gain_stable", "m.music_gain(100.0) == approx(m.music_gain(1.0))")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
