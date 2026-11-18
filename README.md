# pairwise-adaptive-music

战斗切探索时音乐卡半拍、鼓点重叠、淡出断尾：层切换按渲染帧不是音频采样时钟；量化点没对齐小节；淡入淡出用线性振幅不是等功率；战斗强度阈值抖动；横版切换没做预调度；循环点和过渡段 sample 不对齐；多轨 tempo 不同步；暂停时音频时钟继续跑；流式加载在切换点空档；监听器位置影响音乐音量。audio/adaptive_music.py 是核心，tests/test_adaptive_music.py 15个红。要修的是：采样时钟；小节量化；等功率淡变；强度滞回；提前调度；循环对齐；tempo 同步；暂停时钟；过渡预加载；非位听音量。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：音视频处理；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
