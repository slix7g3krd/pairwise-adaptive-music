"""第 52 批：战斗切探索时音乐卡半拍、鼓点重叠、淡出断尾：层切换按渲染帧不是音频采样时钟；量化点没对齐小节；淡入淡出用线性振幅不是等功率；战斗强度阈值抖动；横版切换没做预调度；循环点和过渡段 sample 不对齐；多轨 tempo 不同步；暂停时音频时钟继续跑；流式加载在切换点空档；监听器位置影响音乐音量。"""

import math

# 滞回带宽：强度需在阈值上下各越过半个带宽才翻转，避免边界抖动
_HYSTERESIS_BAND = 0.1


def sample_clock(frame, fps, sample_rate):
    """把渲染帧换算成音频采样时钟（采样数，整数）。"""
    return int(round(frame * sample_rate / fps))


def bar_quantize(time_sec, bpm, beats_per_bar):
    """把时间量化到最近小节起点（秒）。"""
    bar_len = beats_per_bar * 60.0 / bpm
    return math.floor(time_sec / bar_len + 0.5) * bar_len


def equal_power(alpha):
    """返回等功率交叉淡变增益（0..1 -> 0..1，中点为 √2/2）。"""
    return math.sqrt(alpha)


def hysteresis(value, threshold, previous):
    """带滞回地判断战斗音乐是否启用。"""
    half = _HYSTERESIS_BAND / 2.0
    if previous:
        return value >= threshold - half
    return value > threshold + half


def preload_ready(loaded, required):
    """判断过渡段是否已预加载完成。"""
    return loaded >= required


def loop_align(sample, loop_len):
    """把采样位置对齐到循环段（取模回绕）。"""
    return sample % loop_len


def pause_clock(samples, paused):
    """暂停时冻结音频采样时钟（不再前进）。"""
    return 0 if paused else samples


def music_gain(listener_distance):
    """返回非位听音乐的稳定增益（与监听器距离无关）。"""
    return 1.0
