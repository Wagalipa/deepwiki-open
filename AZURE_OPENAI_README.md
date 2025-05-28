# Azure OpenAI 支援說明

本文檔說明如何使用修改後的 `OpenAIClient` 類別來連接 Azure OpenAI 服務。

## 主要改動

1. **新增 Azure OpenAI 客戶端支援**：現在可以同時支援一般的 OpenAI API 和 Azure OpenAI 服務
2. **自動檢測**：根據是否提供 `azure_endpoint` 參數自動選擇使用哪種客戶端
3. **環境變數支援**：支援新的 Azure OpenAI 相關環境變數

## 新增的參數

- `azure_endpoint`: Azure OpenAI 服務的端點 URL
- `api_version`: Azure OpenAI API 版本（預設：2024-02-01）
- `azure_ad_token`: Azure AD 權杖（可選，替代 API key）
- `env_azure_endpoint_name`: Azure 端點環境變數名稱（預設：AZURE_OPENAI_ENDPOINT）
- `env_azure_api_version_name`: Azure API 版本環境變數名稱（預設：AZURE_OPENAI_API_VERSION）

## 使用方式

### 方法 1: 使用環境變數（推薦）

```bash
export AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
export AZURE_OPENAI_API_KEY="your-api-key"
export AZURE_OPENAI_API_VERSION="2024-02-01"  # 可選，有預設值
```

```python
from api.openai_client import OpenAIClient
from adalflow.core import Generator

# 客戶端會自動檢測環境變數並使用 Azure OpenAI
client = OpenAIClient()

generator = Generator(
    model_client=client,
    model_kwargs={"model": "your-deployment-name", "stream": False},
)
```

### 方法 2: 直接設定參數

```python
from api.openai_client import OpenAIClient
from adalflow.core import Generator

# 直接提供 Azure OpenAI 參數
client = OpenAIClient(
    azure_endpoint="https://your-resource.openai.azure.com/",
    api_key="your-api-key",
    api_version="2024-02-01"
)

generator = Generator(
    model_client=client,
    model_kwargs={"model": "your-deployment-name", "stream": False},
)
```

### 方法 3: 使用 Azure AD 權杖

```python
from api.openai_client import OpenAIClient

client = OpenAIClient(
    azure_endpoint="https://your-resource.openai.azure.com/",
    azure_ad_token="your-azure-ad-token",
    api_version="2024-02-01"
)
```

## 環境變數優先順序

對於 Azure OpenAI，API key 的查找順序為：
1. 構造函數中的 `api_key` 參數
2. `OPENAI_API_KEY` 環境變數（如果使用自訂的 `env_api_key_name`）
3. `AZURE_OPENAI_API_KEY` 環境變數

## 注意事項

1. **模型名稱**：在 Azure OpenAI 中，`model` 參數應該是你的部署名稱，而不是原始的模型名稱
2. **端點格式**：Azure 端點 URL 格式為 `https://your-resource.openai.azure.com/`
3. **API 版本**：確保使用正確的 API 版本，推薦使用 `2024-02-01` 或更新版本
4. **向後兼容**：所有現有的 OpenAI 客戶端程式碼都將繼續正常工作

## 測試

執行測試腳本來驗證設定：

```bash
python azure_openai_example.py
```

## 支援的功能

Azure OpenAI 客戶端支援以下功能：
- ✅ 聊天完成（Chat Completions）
- ✅ 嵌入（Embeddings）
- ✅ 串流回應（Streaming）
- ✅ 非同步操作（Async operations）
- ✅ 多模態輸入（Vision models）
- ⚠️ 圖像生成（需要檢查 Azure OpenAI 支援狀況）

## 故障排除

### 常見錯誤

1. **端點 URL 錯誤**
   ```
   ValueError: Environment variable AZURE_OPENAI_ENDPOINT or azure_endpoint must be set for Azure OpenAI
   ```
   解決方案：確保設定了正確的 Azure OpenAI 端點 URL

2. **API 金鑰錯誤**
   ```
   ValueError: Either environment variable OPENAI_API_KEY or AZURE_OPENAI_API_KEY must be set for Azure OpenAI
   ```
   解決方案：設定正確的 API 金鑰環境變數

3. **模型部署名稱錯誤**
   ```
   BadRequestError: The model 'gpt-4o' does not exist
   ```
   解決方案：使用你在 Azure OpenAI 中建立的實際部署名稱

### 檢查清單

- [ ] Azure OpenAI 資源已建立
- [ ] 模型已部署並取得部署名稱
- [ ] API 金鑰已取得
- [ ] 端點 URL 格式正確
- [ ] 環境變數已正確設定
- [ ] 網路連接正常

## 範例程式碼

完整的使用範例請參考 `azure_openai_example.py` 檔案。
