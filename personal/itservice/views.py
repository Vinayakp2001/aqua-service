from django.shortcuts import render

# Create your views here.

# This is dummy data for now. In a real application, you would fetch this from a database.
services_data = {
    "web-development": {
        "title": "Web Development",
        "icon": "fas fa-globe",
        "image": "images/service-webdev.jpg", # Placeholder image
        "description": "Modern, responsive websites that captivate your audience and drive conversions with the latest technologies. Our web development services focus on creating visually stunning, user-friendly, and highly functional websites tailored to your business needs. We use cutting-edge technologies like React, Angular, Vue.js for frontend and Django, Node.js for backend to deliver robust and scalable solutions. From e-commerce platforms to complex web applications, we ensure your online presence stands out.",
        "cost": "Starts from $1500",
        "features": [
            "Custom Website Design",
            "Responsive Development (Desktop, Tablet, Mobile)",
            "E-commerce Solutions",
            "Content Management Systems (CMS)",
            "Performance Optimization",
            "SEO Best Practices"
        ]
    },
    "digital-marketing": {
        "title": "Digital Marketing",
        "icon": "fas fa-chart-line",
        "image": "images/service-marketing.jpg", # Placeholder image
        "description": "Strategic digital marketing campaigns that boost your online presence and generate quality leads. Our comprehensive digital marketing services include Search Engine Optimization (SEO), Social Media Marketing (SMM), Pay-Per-Click (PPC) advertising, content marketing, and email marketing. We craft data-driven strategies to increase your brand visibility, drive targeted traffic, and maximize your return on investment. Let us help you connect with your audience and achieve your marketing goals.",
        "cost": "Custom Quote",
        "features": [
            "Search Engine Optimization (SEO)",
            "Social Media Marketing (SMM)",
            "Pay-Per-Click (PPC) Advertising",
            "Content Marketing",
            "Email Marketing Campaigns",
            "Analytics and Reporting"
        ]
    },
    "mobile-apps": {
        "title": "Mobile Apps",
        "icon": "fas fa-mobile-alt",
        "image": "images/service-mobile.jpg", # Placeholder image
        "description": "Native and cross-platform mobile applications that engage users and grow your business. We specialize in developing high-performance mobile apps for iOS and Android platforms. Whether you need a native app for specific platform advantages or a cross-platform solution for wider reach, our team delivers intuitive and feature-rich applications. We handle everything from concept to deployment, ensuring a seamless user experience and robust functionality.",
        "cost": "Starts from $3000",
        "features": [
            "iOS App Development",
            "Android App Development",
            "Cross-Platform Development (React Native, Flutter)",
            "UI/UX Design for Mobile",
            "Backend Integration",
            "App Store Optimization (ASO)"
        ]
    },
    "cloud-solutions": {
        "title": "Cloud Solutions",
        "icon": "fas fa-cloud",
        "image": "images/service-cloud.jpg", # Placeholder image
        "description": "Scalable cloud infrastructure and migration services for optimal performance and cost-efficiency. Embrace the power of the cloud with our expert solutions. We help businesses design, implement, and manage cloud infrastructures on leading platforms like AWS, Azure, and Google Cloud. Our services include cloud migration, infrastructure as code, cloud security, and cost optimization, ensuring your business leverages the full potential of cloud computing.",
        "cost": "Custom Quote",
        "features": [
            "Cloud Migration Strategy",
            "Infrastructure as a Service (IaaS)",
            "Platform as a Service (PaaS)",
            "Software as a Service (SaaS) Integration",
            "Cloud Security & Compliance",
            "Disaster Recovery & Backup"
        ]
    },
    "cybersecurity": {
        "title": "Cybersecurity",
        "icon": "fas fa-shield-alt",
        "image": "images/service-security.jpg", # Placeholder image
        "description": "Comprehensive security solutions to protect your digital assets and maintain business continuity. In today's threat landscape, robust cybersecurity is paramount. We offer a range of services including vulnerability assessments, penetration testing, security audits, and implementation of advanced security protocols. Our goal is to safeguard your data, applications, and infrastructure from cyber threats, ensuring compliance and peace of mind.",
        "cost": "Starts from $1000",
        "features": [
            "Vulnerability Assessment & Penetration Testing (VAPT)",
            "Security Audits & Compliance",
            "Endpoint Protection",
            "Network Security",
            "Security Information and Event Management (SIEM)",
            "Employee Training & Awareness"
        ]
    },
    "it-consulting": {
        "title": "IT Consulting",
        "icon": "fas fa-cogs",
        "image": "images/service-consulting.jpg", # Placeholder image
        "description": "Expert guidance and strategic planning to optimize your technology infrastructure and processes. Our IT consulting services provide strategic insights and actionable recommendations to align your technology with your business objectives. We help you with IT strategy development, digital transformation, technology assessment, and project management, ensuring you make informed decisions that drive efficiency and innovation.",
        "cost": "Per Hour / Project Based",
        "features": [
            "IT Strategy & Roadmapping",
            "Digital Transformation Consulting",
            "Technology Assessment & Audit",
            "Project Management",
            "Vendor Selection & Management",
            "Business Process Optimization"
        ]
    },
}

def home(request):
    context = {'services': services_data.items()}
    return render(request, 'itservice/home.html', context)

def about(request):
    return render(request, 'itservice/about.html')

def contact(request):
    return render(request, 'itservice/contact.html')

def dashboard(request):
    # Example data (baad me yaha DB ya automation ka data aa sakta hai)
    context = {
        "services_done": 120,
        "services_pending": 30,
        "clients": 15
    }
    return render(request, 'itservice/dashboard.html', context)

def service_detail(request, service_slug):
    # This is dummy data for now. In a real application, you would fetch this from a database.
    service = services_data.get(service_slug)

    if service:
        return render(request, 'itservice/service_detail.html', {'service': service, 'service_image': service['image']})
    else:
        # You might want to render a 404 page or a generic error page here
        return render(request, 'itservice/service_not_found.html', {'service_slug': service_slug})