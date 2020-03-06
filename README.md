# Automatical_Bird
一个利用Pygame制作的简易版Flippy Bird，用作DQN的训练平台。
## 实施策略
DQN Agent以更高的得分为目标，在每一帧，控制Bird的跳跃与否。训练网络接收的参数包括：
- Bird的(x,y)
- 屏幕上两组管道的x坐标，以及管道的间隙上下界
- 当前得分

## 项目依赖
```
pygame
```

## 目标功能：
- [x] 正常的游玩
- [x] 训练接口
- [ ] dqn-Agent训练模块
- [ ] 更好的UI

图片资源来自网络
