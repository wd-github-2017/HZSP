document.addEventListener('DOMContentLoaded', () => {
    const inputText = document.getElementById('input-text');
    const outputContent = document.getElementById('output-content');
    const evaluateBtn = document.getElementById('evaluate-btn');
    const languageSelect = document.getElementById('language-select');

    // 配置marked选项
    marked.setOptions({
        breaks: true,  // 支持GitHub风格的换行
        gfm: true,     // 启用GitHub风格的Markdown
        headerIds: false,  // 禁用标题ID生成
        mangle: false,     // 禁用标题ID混淆
        sanitize: false    // 允许HTML标签
    });

    evaluateBtn.addEventListener('click', async () => {
        const essay = inputText.value.trim();
        if (!essay) {
            alert('请输入需要评价的作文！');
            return;
        }

        // 禁用按钮，防止重复提交
        evaluateBtn.disabled = true;
        outputContent.innerHTML = '<p style="color: #666;">正在评价中...</p>';

        try {
            const response = await fetch('/evaluate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ 
                    essay: essay,
                    language: languageSelect.value 
                }),
            });

            if (!response.ok) {
                throw new Error('评价请求失败');
            }

            const reader = response.body.getReader();
            const decoder = new TextDecoder();
            let markdownContent = '';

            while (true) {
                const { done, value } = await reader.read();
                if (done) break;
                
                const text = decoder.decode(value);
                markdownContent += text;
                // 实时渲染Markdown
                outputContent.innerHTML = marked.parse(markdownContent);
                // 自动滚动到底部
                outputContent.scrollTop = outputContent.scrollHeight;
            }
        } catch (error) {
            console.error('Error:', error);
            outputContent.innerHTML = '<p style="color: #dc3545;">评价过程中发生错误，请重试。</p>';
        } finally {
            evaluateBtn.disabled = false;
        }
    });
}); 