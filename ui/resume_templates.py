def generate_template_1(data):
    """Modern Professional Template"""
    
    html = f"""
    <div style="font-family: 'Segoe UI', Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 40px; background: white; color: #333;">
        <div style="border-bottom: 3px solid #667eea; padding-bottom: 20px; margin-bottom: 25px; text-align: center;">
            <h1 style="color: #2b6cb0; margin-bottom: 10px; font-size: 2.5em;">{data.get('full_name', 'Your Name')}</h1>
            <div style="font-size: 0.9em; color: #4a5568; display: flex; justify-content: center; flex-wrap: wrap; gap: 15px;">
                {f'<span>📧 {data["email"]}</span>' if data.get('email') else ''}
                {f'<span>📱 {data["phone"]}</span>' if data.get('phone') else ''}
                {f'<span>📍 {data["location"]}</span>' if data.get('location') else ''}
                {f'<span>🔗 {data["linkedin"]}</span>' if data.get('linkedin') else ''}
                {f'<span>🌐 {data["portfolio"]}</span>' if data.get('portfolio') else ''}
            </div>
        </div>
    """

    if data.get('summary'):
        html += f"""
        <div style="margin-bottom: 25px;">
            <h2 style="color: #2b6cb0; font-size: 1.4em; border-bottom: 1px solid #e2e8f0; padding-bottom: 5px; margin-bottom: 10px;">Professional Summary</h2>
            <p style="line-height: 1.6;">{data['summary']}</p>
        </div>
        """

    if data.get('experiences') and any(exp.get('title') for exp in data['experiences']):
        html += """
        <div style="margin-bottom: 25px;">
            <h2 style="color: #2b6cb0; font-size: 1.4em; border-bottom: 1px solid #e2e8f0; padding-bottom: 5px; margin-bottom: 15px;">Work Experience</h2>
        """
        for exp in data['experiences']:
            if exp.get('title') or exp.get('company'):
                html += f"""
                <div style="margin-bottom: 15px;">
                    <div style="display: flex; justify-content: space-between; align-items: baseline;">
                        <strong style="font-size: 1.1em;">{exp.get('title', '')}</strong>
                        <span style="color: #718096; font-size: 0.9em;">{exp.get('duration', '')}</span>
                    </div>
                    <div style="color: #4a5568; font-weight: 500; margin-bottom: 5px;">{exp.get('company', '')}</div>
                    <p style="line-height: 1.5; margin-top: 5px; white-space: pre-wrap;">{exp.get('description', '')}</p>
                </div>
                """
        html += "</div>"

    if data.get('education') and any(edu.get('degree') for edu in data['education']):
        html += """
        <div style="margin-bottom: 25px;">
            <h2 style="color: #2b6cb0; font-size: 1.4em; border-bottom: 1px solid #e2e8f0; padding-bottom: 5px; margin-bottom: 15px;">Education</h2>
        """
        for edu in data['education']:
            if edu.get('degree') or edu.get('institution'):
                html += f"""
                <div style="margin-bottom: 10px; display: flex; justify-content: space-between; align-items: baseline;">
                    <div>
                        <strong>{edu.get('degree', '')}</strong>
                        <div style="color: #4a5568;">{edu.get('institution', '')}</div>
                    </div>
                    <span style="color: #718096; font-size: 0.9em;">{edu.get('year', '')}</span>
                </div>
                """
        html += "</div>"
        
    if data.get('skills') and any(data['skills']):
        html += f"""
        <div style="margin-bottom: 25px;">
            <h2 style="color: #2b6cb0; font-size: 1.4em; border-bottom: 1px solid #e2e8f0; padding-bottom: 5px; margin-bottom: 10px;">Skills</h2>
            <p style="line-height: 1.6;">{', '.join(data['skills'])}</p>
        </div>
        """

    if data.get('projects') and any(proj.get('name') for proj in data['projects']):
        html += """
        <div style="margin-bottom: 25px;">
            <h2 style="color: #2b6cb0; font-size: 1.4em; border-bottom: 1px solid #e2e8f0; padding-bottom: 5px; margin-bottom: 15px;">Projects</h2>
        """
        for proj in data['projects']:
            if proj.get('name'):
                html += f"""
                <div style="margin-bottom: 10px;">
                    <strong>{proj.get('name', '')}</strong>
                    <p style="line-height: 1.5; margin-top: 5px; white-space: pre-wrap;">{proj.get('description', '')}</p>
                </div>
                """
        html += "</div>"

    if data.get('certifications') and any(data['certifications']):
        html += f"""
        <div style="margin-bottom: 25px;">
            <h2 style="color: #2b6cb0; font-size: 1.4em; border-bottom: 1px solid #e2e8f0; padding-bottom: 5px; margin-bottom: 10px;">Certifications</h2>
            <ul style="margin: 0; padding-left: 20px;">
                {''.join(f'<li style="margin-bottom: 5px;">{cert}</li>' for cert in data['certifications'] if cert)}
            </ul>
        </div>
        """

    html += "</div>"
    return html

def generate_template_2(data):
    """Minimalist Elegant Template"""
    
    html = f"""
    <div style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 40px; background: white; color: #222;">
        <div style="text-align: left; margin-bottom: 30px;">
            <h1 style="font-size: 2.2em; font-weight: 300; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 15px;">{data.get('full_name', 'YOUR NAME')}</h1>
            
            <div style="font-size: 0.9em; color: #666; display: flex; flex-wrap: wrap; gap: 10px; border-top: 1px solid #eee; padding-top: 10px;">
                {' &bull; '.join([x for x in [data.get('email'), data.get('phone'), data.get('location')] if x])}
                {' | '.join([x for x in [data.get('linkedin'), data.get('portfolio')] if x and len([y for y in [data.get('email'), data.get('phone'), data.get('location')] if y]) == 0])}
            </div>
            {f'<div style="font-size: 0.9em; color: #666; margin-top: 5px;">{" | ".join([x for x in [data.get("linkedin"), data.get("portfolio")] if x])}</div>' if any([data.get('linkedin'), data.get('portfolio')]) and any([data.get('email'), data.get('phone'), data.get('location')]) else ''}
        </div>
    """

    if data.get('summary'):
        html += f"""
        <div style="margin-bottom: 30px;">
            <p style="line-height: 1.8; font-size: 1em; color: #444; font-style: italic;">{data['summary']}</p>
        </div>
        """

    if data.get('experiences') and any(exp.get('title') for exp in data['experiences']):
        html += """
        <div style="margin-bottom: 30px;">
            <h2 style="font-size: 1.2em; text-transform: uppercase; letter-spacing: 1px; color: #000; border-bottom: 1px solid #000; padding-bottom: 5px; margin-bottom: 20px;">Experience</h2>
        """
        for exp in data['experiences']:
            if exp.get('title') or exp.get('company'):
                html += f"""
                <div style="margin-bottom: 20px;">
                    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 5px;">
                        <span style="font-weight: bold; font-size: 1.1em;">{exp.get('title', '')} <span style="font-weight: normal; color: #666;">at {exp.get('company', '')}</span></span>
                        <span style="font-size: 0.9em; color: #888;">{exp.get('duration', '')}</span>
                    </div>
                    <p style="line-height: 1.6; margin-top: 5px; color: #444; white-space: pre-wrap;">{exp.get('description', '')}</p>
                </div>
                """
        html += "</div>"

    if data.get('education') and any(edu.get('degree') for edu in data['education']):
        html += """
        <div style="margin-bottom: 30px;">
            <h2 style="font-size: 1.2em; text-transform: uppercase; letter-spacing: 1px; color: #000; border-bottom: 1px solid #000; padding-bottom: 5px; margin-bottom: 20px;">Education</h2>
        """
        for edu in data['education']:
            if edu.get('degree') or edu.get('institution'):
                html += f"""
                <div style="margin-bottom: 15px; display: flex; justify-content: space-between; align-items: baseline;">
                    <div>
                        <strong style="font-size: 1.05em;">{edu.get('degree', '')}</strong>
                        <div style="color: #666; margin-top: 3px;">{edu.get('institution', '')}</div>
                    </div>
                    <span style="font-size: 0.9em; color: #888;">{edu.get('year', '')}</span>
                </div>
                """
        html += "</div>"
        
    if data.get('skills') and any(data['skills']):
        html += f"""
        <div style="margin-bottom: 30px;">
            <h2 style="font-size: 1.2em; text-transform: uppercase; letter-spacing: 1px; color: #000; border-bottom: 1px solid #000; padding-bottom: 5px; margin-bottom: 15px;">Skills</h2>
            <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                {''.join(f'<span style="background: #f5f5f5; padding: 5px 12px; border-radius: 3px; font-size: 0.9em; color: #333;">{skill}</span>' for skill in data['skills'] if skill)}
            </div>
        </div>
        """

    if data.get('projects') and any(proj.get('name') for proj in data['projects']):
        html += """
        <div style="margin-bottom: 30px;">
            <h2 style="font-size: 1.2em; text-transform: uppercase; letter-spacing: 1px; color: #000; border-bottom: 1px solid #000; padding-bottom: 5px; margin-bottom: 20px;">Projects</h2>
        """
        for proj in data['projects']:
            if proj.get('name'):
                html += f"""
                <div style="margin-bottom: 15px;">
                    <strong style="font-size: 1.05em;">{proj.get('name', '')}</strong>
                    <p style="line-height: 1.6; margin-top: 5px; color: #444; white-space: pre-wrap;">{proj.get('description', '')}</p>
                </div>
                """
        html += "</div>"

    if data.get('certifications') and any(data['certifications']):
        html += f"""
        <div style="margin-bottom: 30px;">
            <h2 style="font-size: 1.2em; text-transform: uppercase; letter-spacing: 1px; color: #000; border-bottom: 1px solid #000; padding-bottom: 5px; margin-bottom: 15px;">Certifications</h2>
            <p style="line-height: 1.6; color: #444;">{' &bull; '.join([cert for cert in data['certifications'] if cert])}</p>
        </div>
        """

    html += "</div>"
    return html

def generate_template_3(data):
    """Creative Bold Template"""
    
    html = f"""
    <div style="font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 0; background: white; color: #333; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
        <div style="background-color: #2c3e50; color: white; padding: 40px; text-align: center;">
            <h1 style="margin: 0 0 15px 0; font-size: 3em; letter-spacing: 1px; color: #ecf0f1;">{data.get('full_name', 'Your Name')}</h1>
            
            <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 15px; font-size: 0.95em; color: #bdc3c7;">
                {f'<span><strong style="color: #e74c3c;">E:</strong> {data["email"]}</span>' if data.get('email') else ''}
                {f'<span><strong style="color: #e74c3c;">P:</strong> {data["phone"]}</span>' if data.get('phone') else ''}
                {f'<span><strong style="color: #e74c3c;">L:</strong> {data["location"]}</span>' if data.get('location') else ''}
            </div>
            {f'<div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 15px; font-size: 0.95em; color: #bdc3c7; margin-top: 10px;">' if any([data.get('linkedin'), data.get('portfolio')]) else ''}
                {f'<span><strong style="color: #e74c3c;">IN:</strong> {data["linkedin"]}</span>' if data.get('linkedin') else ''}
                {f'<span><strong style="color: #e74c3c;">W:</strong> {data["portfolio"]}</span>' if data.get('portfolio') else ''}
            {f'</div>' if any([data.get('linkedin'), data.get('portfolio')]) else ''}
        </div>
        
        <div style="padding: 40px;">
    """

    if data.get('summary'):
        html += f"""
        <div style="margin-bottom: 30px; background: #fdfefe; padding: 20px; border-left: 4px solid #e74c3c; border-radius: 0 5px 5px 0;">
            <p style="margin: 0; line-height: 1.7; font-size: 1.05em; color: #34495e;">{data['summary']}</p>
        </div>
        """

    st_col = "display: grid; grid-template-columns: 200px 1fr; gap: 20px;"

    if data.get('experiences') and any(exp.get('title') for exp in data['experiences']):
        html += f"""
        <div style="margin-bottom: 35px; {{st_col}}">
            <div style="width: 150px; float: left; padding-right: 20px;">
                <h2 style="color: #2c3e50; font-size: 1.5em; text-transform: uppercase; margin-top: 0; text-align: right;">Experience</h2>
            </div>
            <div style="margin-left: 170px;">
        """
        for exp in data['experiences']:
            if exp.get('title') or exp.get('company'):
                html += f"""
                <div style="margin-bottom: 25px; position: relative;">
                    <div style="position: absolute; left: -25px; top: 6px; width: 10px; height: 10px; border-radius: 50%; background: #e74c3c;"></div>
                    <div style="background: #f8f9fa; padding: 15px; border-radius: 5px;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px; flex-wrap: wrap;">
                            <strong style="font-size: 1.2em; color: #2c3e50;">{exp.get('title', '')}</strong>
                            <span style="color: #e74c3c; font-weight: bold; font-size: 0.9em; background: #fadbd8; padding: 3px 8px; border-radius: 12px;">{exp.get('duration', '')}</span>
                        </div>
                        <div style="color: #7f8c8d; font-size: 1.05em; margin-bottom: 10px; font-weight: bold;">{exp.get('company', '')}</div>
                        <p style="margin: 0; line-height: 1.6; color: #555; white-space: pre-wrap;">{exp.get('description', '')}</p>
                    </div>
                </div>
                """
        html += "</div><div style='clear: both;'></div></div>"

    if data.get('education') and any(edu.get('degree') for edu in data['education']):
        html += f"""
        <div style="margin-bottom: 35px; {{st_col}}">
            <div style="width: 150px; float: left; padding-right: 20px;">
                <h2 style="color: #2c3e50; font-size: 1.5em; text-transform: uppercase; margin-top: 0; text-align: right;">Education</h2>
            </div>
            <div style="margin-left: 170px;">
        """
        for edu in data['education']:
            if edu.get('degree') or edu.get('institution'):
                html += f"""
                <div style="margin-bottom: 20px; border-bottom: 1px dotted #ccc; padding-bottom: 15px;">
                    <div style="display: flex; justify-content: space-between; align-items: baseline;">
                        <strong style="font-size: 1.15em; color: #2c3e50;">{edu.get('degree', '')}</strong>
                        <span style="color: #e74c3c; font-weight: bold; font-size: 0.9em;">{edu.get('year', '')}</span>
                    </div>
                    <div style="color: #7f8c8d; margin-top: 5px;">{edu.get('institution', '')}</div>
                </div>
                """
        html += "</div><div style='clear: both;'></div></div>"
        
    if data.get('skills') and any(data['skills']):
        html += f"""
        <div style="margin-bottom: 35px; {{st_col}}">
            <div style="width: 150px; float: left; padding-right: 20px;">
                <h2 style="color: #2c3e50; font-size: 1.5em; text-transform: uppercase; margin-top: 0; text-align: right;">Expertise</h2>
            </div>
            <div style="margin-left: 170px;">
                <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                    {''.join(f'<span style="background: #2c3e50; color: white; padding: 8px 15px; border-radius: 20px; font-size: 0.95em;">{skill}</span>' for skill in data['skills'] if skill)}
                </div>
            </div><div style='clear: both;'></div>
        </div>
        """

    if data.get('projects') and any(proj.get('name') for proj in data['projects']):
        html += f"""
        <div style="margin-bottom: 35px; {{st_col}}">
            <div style="width: 150px; float: left; padding-right: 20px;">
                <h2 style="color: #2c3e50; font-size: 1.5em; text-transform: uppercase; margin-top: 0; text-align: right;">Projects</h2>
            </div>
            <div style="margin-left: 170px;">
        """
        for proj in data['projects']:
            if proj.get('name'):
                html += f"""
                <div style="margin-bottom: 20px; background: #ecf0f1; padding: 15px; border-radius: 5px; border-left: 3px solid #3498db;">
                    <strong style="color: #2c3e50; font-size: 1.1em; display: block; margin-bottom: 5px;">{proj.get('name', '')}</strong>
                    <p style="margin: 0; line-height: 1.5; color: #555; white-space: pre-wrap;">{proj.get('description', '')}</p>
                </div>
                """
        html += "</div><div style='clear: both;'></div></div>"

    if data.get('certifications') and any(data['certifications']):
        html += f"""
        <div style="margin-bottom: 20px; {{st_col}}">
            <div style="width: 150px; float: left; padding-right: 20px;">
                <h2 style="color: #2c3e50; font-size: 1.5em; text-transform: uppercase; margin-top: 0; text-align: right;">Awards</h2>
            </div>
            <div style="margin-left: 170px;">
                <ul style="margin: 0; padding-left: 20px; color: #34495e; line-height: 1.6;">
                    {''.join(f'<li style="margin-bottom: 8px;">{cert}</li>' for cert in data['certifications'] if cert)}
                </ul>
            </div><div style='clear: both;'></div>
        </div>
        """

    html += """
        </div>
    </div>
    """
    return html

def generate_template_4(data):
    """Executive Classic Template"""
    
    html = f"""
    <div style="font-family: 'Times New Roman', Times, serif; max-width: 800px; margin: 0 auto; padding: 40px; background: white; color: #000;">
        <div style="text-align: center; border-bottom: 2px solid #000; padding-bottom: 15px; margin-bottom: 20px;">
            <h1 style="margin: 0 0 10px 0; font-size: 2.8em; font-weight: normal; text-transform: uppercase;">{data.get('full_name', 'Your Name')}</h1>
            
            <div style="font-size: 1em; margin-bottom: 5px;">
                {' | '.join([x for x in [data.get('location')] if x])}
            </div>
            <div style="font-size: 1em;">
                {' | '.join([x for x in [data.get('phone'), data.get('email')] if x])}
            </div>
            <div style="font-size: 1em; margin-top: 5px;">
                {' | '.join([x for x in [data.get('linkedin'), data.get('portfolio')] if x])}
            </div>
        </div>
    """

    if data.get('summary'):
        html += f"""
        <div style="margin-bottom: 20px;">
            <h2 style="font-size: 1.2em; text-transform: uppercase; border-bottom: 1px solid #000; margin-bottom: 10px; padding-bottom: 3px;">Summary</h2>
            <p style="margin: 0; line-height: 1.5; font-size: 1.05em; text-align: justify;">{data['summary']}</p>
        </div>
        """

    if data.get('experiences') and any(exp.get('title') for exp in data['experiences']):
        html += """
        <div style="margin-bottom: 20px;">
            <h2 style="font-size: 1.2em; text-transform: uppercase; border-bottom: 1px solid #000; margin-bottom: 15px; padding-bottom: 3px;">Professional Experience</h2>
        """
        for exp in data['experiences']:
            if exp.get('title') or exp.get('company'):
                html += f"""
                <div style="margin-bottom: 15px;">
                    <div style="display: flex; justify-content: space-between; align-items: baseline;">
                        <div>
                            <strong style="font-size: 1.1em;">{exp.get('company', '')}</strong>
                        </div>
                        <span style="font-style: italic;">{exp.get('duration', '')}</span>
                    </div>
                    <div style="font-style: italic; margin-bottom: 5px;">{exp.get('title', '')}</div>
                    <ul style="margin: 0; padding-left: 20px; line-height: 1.5;">
                        {''.join(f'<li>{p.strip()}</li>' for p in exp.get('description', '').split(chr(10)) if p.strip()) if exp.get('description') else ''}
                    </ul>
                </div>
                """
        html += "</div>"

    if data.get('education') and any(edu.get('degree') for edu in data['education']):
        html += """
        <div style="margin-bottom: 20px;">
            <h2 style="font-size: 1.2em; text-transform: uppercase; border-bottom: 1px solid #000; margin-bottom: 15px; padding-bottom: 3px;">Education</h2>
        """
        for edu in data['education']:
            if edu.get('degree') or edu.get('institution'):
                html += f"""
                <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 10px;">
                    <div>
                        <strong style="font-size: 1.05em;">{edu.get('institution', '')}</strong>
                        <div>{edu.get('degree', '')}</div>
                    </div>
                    <span style="font-style: italic;">{edu.get('year', '')}</span>
                </div>
                """
        html += "</div>"
        
    if data.get('skills') and any(data['skills']):
        html += f"""
        <div style="margin-bottom: 20px;">
            <h2 style="font-size: 1.2em; text-transform: uppercase; border-bottom: 1px solid #000; margin-bottom: 10px; padding-bottom: 3px;">Core Competencies</h2>
            <div style="line-height: 1.5;">
                {' &bull; '.join([skill for skill in data['skills'] if skill])}
            </div>
        </div>
        """

    if data.get('projects') and any(proj.get('name') for proj in data['projects']):
        html += """
        <div style="margin-bottom: 20px;">
            <h2 style="font-size: 1.2em; text-transform: uppercase; border-bottom: 1px solid #000; margin-bottom: 10px; padding-bottom: 3px;">Selected Projects</h2>
        """
        for proj in data['projects']:
            if proj.get('name'):
                html += f"""
                <div style="margin-bottom: 10px;">
                    <strong>{proj.get('name', '')}</strong>
                    <div style="margin: 0; line-height: 1.5; display: inline;"> - {proj.get('description', '')}</div>
                </div>
                """
        html += "</div>"

    if data.get('certifications') and any(data['certifications']):
        html += f"""
        <div style="margin-bottom: 20px;">
            <h2 style="font-size: 1.2em; text-transform: uppercase; border-bottom: 1px solid #000; margin-bottom: 10px; padding-bottom: 3px;">Certifications</h2>
            <div style="line-height: 1.5;">
                {', '.join([cert for cert in data['certifications'] if cert])}
            </div>
        </div>
        """

    html += "</div>"
    return html
