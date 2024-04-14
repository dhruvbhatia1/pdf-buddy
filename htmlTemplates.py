css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn5.vectorstock.com/i/1000x1000/31/54/bot-sign-design-robot-logo-template-modern-flat-vector-27973154.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://imgs.search.brave.com/gQSTf1tTr3I6p1CBOz7D_yH9aPgD4HFEi0fsSP5hFuI/rs:fit:860:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzA3LzY4LzI1Lzk1/LzM2MF9GXzc2ODI1/OTU5NV9XS1dhTHlT/MVh5T3FvS3hWbVFH/Slk2WmxuSWtHbWh4/Qi5qcGc">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''