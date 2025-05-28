#!/usr/bin/env python3
"""
Azure OpenAI Client 使用範例

這個腳本展示如何使用修改後的 OpenAIClient 類別來連接 Azure OpenAI 服務。

環境變數設置：
export AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
export AZURE_OPENAI_API_KEY="your-api-key"
export AZURE_OPENAI_API_VERSION="2024-02-01"

或者直接在程式碼中設定參數。
"""

import os
from api.openai_client import OpenAIClient
from adalflow.core import Generator

def test_azure_openai():
    """測試 Azure OpenAI 連接"""
    print("正在測試 Azure OpenAI 連接...")
    
    # 方法 1: 使用環境變數
    if all([
        os.getenv("AZURE_OPENAI_ENDPOINT"),
        os.getenv("AZURE_OPENAI_API_KEY"),
    ]):
        print("使用環境變數設定...")
        client = OpenAIClient()
        
    # 方法 2: 直接設定參數
    else:
        print("請設定以下環境變數或直接在程式碼中提供參數：")
        print("AZURE_OPENAI_ENDPOINT")
        print("AZURE_OPENAI_API_KEY")
        print("AZURE_OPENAI_API_VERSION (可選，預設為 2024-02-01)")
        
        # 如果你想直接在程式碼中設定，請取消註解並填入正確的值：
        # client = OpenAIClient(
        #     azure_endpoint="https://your-resource.openai.azure.com/",
        #     api_key="your-api-key",
        #     api_version="2024-02-01"
        # )
        return
    
    # 建立生成器
    generator = Generator(
        model_client=client,
        model_kwargs={
            "model": "gpt-4o",  # 使用你的 Azure 部署名稱
            "stream": False,
            "max_tokens": 100
        },
    )
    
    # 測試請求
    prompt_kwargs = {"input_str": "你好，請簡單介紹一下 Azure OpenAI 服務。"}
    
    try:
        response = generator(prompt_kwargs)
        print(f"Azure OpenAI 回應: {response}")
        print("✅ Azure OpenAI 連接成功！")
    except Exception as e:
        print(f"❌ 連接失敗: {e}")

def test_regular_openai():
    """測試一般的 OpenAI 連接（作為對比）"""
    print("\n正在測試一般 OpenAI 連接...")
    
    if not os.getenv("OPENAI_API_KEY"):
        print("請設定 OPENAI_API_KEY 環境變數")
        return
    
    # 建立一般的 OpenAI 客戶端
    client = OpenAIClient()
    
    generator = Generator(
        model_client=client,
        model_kwargs={
            "model": "gpt-4o-mini",
            "stream": False,
            "max_tokens": 100
        },
    )
    
    prompt_kwargs = {"input_str": "Hello, please briefly introduce OpenAI."}
    
    try:
        response = generator(prompt_kwargs)
        print(f"OpenAI 回應: {response}")
        print("✅ OpenAI 連接成功！")
    except Exception as e:
        print(f"❌ 連接失敗: {e}")

if __name__ == "__main__":
    print("=== OpenAI Client Azure 支援測試 ===\n")
    
    # 測試 Azure OpenAI
    test_azure_openai()
    
    # 測試一般 OpenAI
    test_regular_openai()
    
    print("\n=== 測試完成 ===")
