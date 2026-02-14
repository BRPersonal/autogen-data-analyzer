from autogen_agentchat.agents import CodeExecutorAgent
import asyncio
import traceback
from pathlib import Path
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
import warnings 


def getCodeExecutorAgent(code_executor):

    code_executor_agent = CodeExecutorAgent(
        name='CodeExecutor',
        code_executor = code_executor,
        supported_languages=["python", "sh", "bash"]
    )

    return code_executor_agent


async def main():
    # Ensure workdir exists
    work_dir = Path('workdir')
    work_dir.mkdir(exist_ok=True)

    docker=DockerCommandLineCodeExecutor(
      work_dir=work_dir,
      timeout=120
    )

    code_executor_agent = getCodeExecutorAgent(docker)

    task = TextMessage(
            content=''' Here is the Python Code which You have to run.
```python
print('Hello Krishna')
````        
    ''',
        source='User'
    )


    try:
      await docker.start()

      res = await code_executor_agent.on_messages(
          messages=[task],
          cancellation_token=CancellationToken()
      )
      print('result is :', res.chat_message.content)
      if res.inner_messages:
          print('inner messages:', res.inner_messages)

    except Exception as e:
      print(f"Error: {e}")
      print("\nFull traceback:")
      traceback.print_exc()
      raise e
    finally:
      try:
        await docker.stop()
        print("docker conainer stopped")
      except Exception as e:
        print(f"Error stopping docker: {e}")

if (__name__ == '__main__'):
  
    #suppress warnings
    warnings.filterwarnings('ignore')  
    asyncio.run(main())

    