def generate_template_1(data):
    """Modern Professional Template"""
    html = f"""
    <div style="font-family: 'Segoe UI', Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 40px; background: white;">
        <div style="border-bottom: 3px solid #667eea; padding-bottom: 20px; margin-bottom: 25px;">
            <h1>{data['full_name'] or 'Your Name'}</h1>

            <div>
                {f'<span>📧 {data["email"]}</span>' if data['email'] else ''}
                {f'<span>📱 {data["phone"]}</span>' if data['phone'] else ''}
                {f'<span>📍 {data["location"]}</span>' if data['location'] else ''}
            </div>

            <div>
                {f'<span>🔗 {data["linkedin"]}</span>' if data['linkedin'] else ''}
                {f'<span>🌐 {data["portfolio"]}</span>' if data['portfolio'] else ''}
            </div>
        </div>
    </div>
    """
    return html

def generate_template_2(data):
    """Minimalist Elegant Template"""
    html = f"""
    <div>
        <h1>{data['full_name'].upper() or 'YOUR NAME'}</h1>

        <div>
            {' &bull; '.join([x for x in [data['email'], data['phone'], data['location']] if x])}
        </div>

        <div>
            {' | '.join([x for x in [data['linkedin'], data['portfolio']] if x])}
        </div>

        {f'<p>{data["summary"]}</p>' if data['summary'] else ''}

        {f'''
        <p>{' &bull; '.join(data['skills'])}</p>
        ''' if data['skills'] else ''}
    </div>
    """
    return html

def generate_template_3(data):
    """Creative Bold Template"""
    html = f"""
    <div>
        <h1>{data['full_name'] or 'Your Name'}</h1>

        <div>
            {data['email']} {f'&bull; {data["phone"]}' if data['phone'] else ''}
        </div>

        <div>
            {data['location']}
        </div>

        <div>
            {data['linkedin']} {f'&bull; {data["portfolio"]}' if data['portfolio'] else ''}
        </div>
    </div>
    """
    return html

def generate_template_4(data):
    """Executive Classic Template"""
    html = f"""
    <div>
        <h1>{data['full_name'] or 'Your Name'}</h1>

        <div>
            {data['email']}
            {f' | {data["phone"]}' if data['phone'] else ''}
        </div>

        {f'''
        <div>
            {''.join([f'<span>&bull; {skill}</span>' for skill in data['skills']])}
        </div>
        ''' if data['skills'] else ''}
    </div>
    """
    return html
