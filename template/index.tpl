%include('template/header.tpl', title='')
        <div class="container" role="main">
            %include('template/title.tpl')

            <div class="row">
                <div class="col-md-offset-4 col-md-4 col-xs-offset-1 col-xs-10  text-center">
                    <p>Pressione o botão para alterar o estado do LED.</p>
                    <p><button id="led1" type="button" class="btn btn-lg btn-block" onClick='changeStatus();'>conectando</button></p>
                    <p id="conn-log">conectando</p>
                </div>
            </div>

            <div class="row text-center">
                <p><a href="https://github.com/plainspooky/led_blink" target="_BLANK"><img src="static/led_blink.png"/><br/>
                    código fonte do <strong>LED blink</strong>.</a>
                </p>
            </div>
        </div>
%include('template/footer.tpl',js='index.js')
