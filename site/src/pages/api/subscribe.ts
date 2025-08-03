import type { APIRoute } from 'astro';

export const POST: APIRoute = async ({ request }) => {
  console.log('API endpoint called');
  
  try {
    const body = await request.json();
    console.log('Request body:', body);
    
    const { email } = body;
    
    if (!email) {
      console.log('No email provided');
      return new Response(JSON.stringify({ error: 'Email is required' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
    const BUTTONDOWN_API = import.meta.env.BUTTONDOWN_API;
    console.log('API key exists:', !!BUTTONDOWN_API);
    
    if (!BUTTONDOWN_API) {
      console.error('BUTTONDOWN_API environment variable is not set');
      return new Response(JSON.stringify({ error: 'Server configuration error' }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
    console.log('Making request to Buttondown API');
    
    const response = await fetch('https://api.buttondown.email/v1/subscribers', {
      method: 'POST',
      headers: {
        'Authorization': `Token ${BUTTONDOWN_API}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: email,
        tags: ['lifeline', 'blood-testing', 'newsletter']
      }),
    });
    
    console.log('Buttondown response status:', response.status);
    
    if (response.ok) {
      console.log('Subscription successful');
      return new Response(JSON.stringify({ success: true }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
      });
    } else {
      const errorData = await response.json();
      console.error('Buttondown API error:', errorData);
      
      return new Response(JSON.stringify({ 
        error: 'Failed to subscribe. Please try again.' 
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
  } catch (error) {
    console.error('Subscription error:', error);
    return new Response(JSON.stringify({ 
      error: 'Server error. Please try again.' 
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}; 