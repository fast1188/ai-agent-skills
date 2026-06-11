# Test Generation Prompt Template

为以下代码生成单元测试,要求:

1. **覆盖率 ≥ 80%**
2. **测试用例**:
   - 正常情况
   - 边界条件(空、null、最大、最小)
   - 异常情况(错误输入、异常抛出)
3. **命名规范**:`test_<函数>_<场景>_<预期>`
4. **使用 pytest**(如 Python)
5. **mock 外部依赖**

输出格式:
```python
def test_function_name_scenario_expected():
    # Arrange
    # Act
    # Assert
```