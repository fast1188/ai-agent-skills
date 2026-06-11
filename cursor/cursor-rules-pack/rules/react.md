# Cursor React Project Rules

# 组件
- 函数组件优先,不用 class 组件
- 组件名:PascalCase
- Props:interface 定义,export 出去
- 组件文件:PascalCase.tsx

# Hooks
- 命名:useXxx
- 遵守 hooks 规则(只在顶层调用)
- 自定义 hooks 抽到 hooks/ 目录

# 状态管理
- 简单用 useState
- 跨组件用 Context
- 复杂用 Zustand / Redux Toolkit

# 样式
- Tailwind CSS 优先
- 不用 inline style
- 组件级样式用 CSS Modules

# 测试
- Vitest + React Testing Library
- 组件测试覆盖 props / events / states

# 性能
- React.memo 包裹昂贵组件
- useMemo / useCallback 适当使用
- 不要过早优化

# 目录
src/
├── components/  # 复用组件
├── pages/       # 路由页面
├── hooks/       # 自定义 hooks
├── utils/       # 工具函数
└── types/       # TS 类型